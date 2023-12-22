require('dotenv').config();
const express = require('express')
const cookieParser = require('cookie-parser')
const jwt = require('./util/jwt_utils')
const connection = require('./util/DB')
const axios = require('axios')
const crypto = require('crypto');

const app = express()
app.set("view engine", "ejs");
app.use(cookieParser())
app.use(express.json())
app.use(express.urlencoded({ extended: false }));
app.use(express.static('public'));
app.set('views', './public');

app.get('/', jwt.verify, (req, res) => {
	let flag = "Please Login"

	if(req.jwt.isLogin){
		if(req.jwt.idx=="admin") flag = process.env.FLAG
		else flag = "You are not admin."
		res.render('index', {isLogin: req.jwt.isLogin, name: req.jwt.idx, flag: flag})
	}
	else{
		res.render('index', {isLogin: req.jwt.isLogin, name: 'Anonymous', flag: flag})
	}
})

app.get('/login', (req, res) => {res.render('login')})
app.post('/login', async (req, res) => {
	const host = req.get('HOST')
	const id = req.body.id
	const password = req.body.password
	const url = encodeURI(`http://${host}/password/${id}`)

	const resp = await axios.get(url)

	if(resp.data === "User Does Not Exist") {
		res.write("<script>alert('please register')</script>")
		res.write("<script>window.location='/register'</script>")
		res.send()
	}
	else if(resp.data === "500 Error" || resp.data === undefined) 
	{
		res.send("SomeThind Error")
	}
	else if(resp.data === crypto.createHash('SHA256').update(password).digest('hex')) {
		const token = jwt.genarateAccessToken(id)
		res.cookie('token', token)
		res.redirect('/')
	}
	else {
		res.write("<script>alert('Incorrect Id or Password')</script>")
		res.write("<script>window.location='/login'</script>")
		res.send()
	}
})
app.get('/password/:id', async (req, res) => {
	const sql = "SELECT password FROM login WHERE id = ?"
	const values = [req.params.id]

	try {
		const [password] = await connection.execute(sql, values)
		if(password.length == 0) return res.send("User Does Not Exist")
		return res.send(password[0]['password'])
	} catch(err) {
		return res.send("500 Error")
	}
	
})
app.get('/register', (req, res) => {res.render('register')})
app.post('/register', async (req, res, next) => {
	const id = req.body.id
	const password = req.body.password

	const sql = "INSERT INTO login(id, password) VALUES(?, SHA2(?, 256))"
	const values = [id, password]

	try{
		await connection.execute(sql, values)
		res.write("<script>alert('Success to Register.\\nPlease Login.')</script>")
		res.write("<script>window.location='/login'</script>")
		res.send()
	}catch(err){
		if(err.code == "ER_DUP_ENTRY") {
			res.write("<script>alert('Id already exist.')</script>")
			res.write("<script>window.location='/register'</script>")
			res.send()
		}
		else if(err.code == "ER_DATA_TOO_LONG") {
			res.write("<script>alert('Id is too long.')</script>")
			res.write("<script>window.location='/register'</script>")
			res.send()
		}
		else {
			console.log(err)
			next(err)
		}
	}
})
app.get('/logout', (req, res) => {res.clearCookie('token'); res.redirect('/')})

app.use((err, req, res, next) => {
	console.error(err.stack)
	res.status(500).send("SomeThing Error");
})

app.listen(process.env.PORT);