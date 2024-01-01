require('dotenv').config()
const jwt = require('jsonwebtoken')

let jwt_utils = {
	genarateAccessToken : (id, name) => {
	return jwt.sign({
			idx: id,
		},
			process.env.JWT_SECRET_CODE,
			{
			algorithm : "HS256",
			expiresIn : "20m",
			issuer : "ksh30918"
		})
	},

	verify: function(req, res, next) {
		if(!req.cookies.token) {
			req.jwt = {isLogin: false}
			next();
		}
		else {
			token = req.cookies.token
			jwt.verify(token, process.env.JWT_SECRET_CODE, (err, decoded) => {
				if(err){
					res.write("<script>alert('please login again')</script>")
					res.write("<script>window.location='/login'</script>")
					res.send()
					next('route');
				}
				else{
					req.jwt = decoded
					req.jwt.isLogin = true
					next()
				}
			})
		}
	}
}

module.exports = jwt_utils;