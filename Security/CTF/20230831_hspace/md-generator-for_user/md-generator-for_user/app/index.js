const express       = require('express');
const session       = require('express-session');
const bodyParser    = require('body-parser');
const crypto        = require('crypto');
const uuid			= require('uuid4');
const turndown		= require('turndown');
const { visit }		= require('./bot');
const report 		= new Map();
const now			= () => { return Math.floor(+new Date()/1000); }

const app = express();
const Turndown = new turndown();

const users = new Map([
    []
]);

const markdown = new Map([
    []
]);

const shared_markdown = new Map([
    []
]);

app.use('/static', express.static('static'))
app.set("view engine", "ejs");
app.engine("html", require("ejs").renderFile);  

app.use(bodyParser.urlencoded({ extended: false }));
app.use(
    session({
        cookie: { maxAge : 600000 },
        secret: crypto.randomBytes(64).toString(),
    })
);

app.all('/', (req, res) => {
	if (!req.session.username)
		return res.redirect("/login");

	return res.render("index", { username: req.session.username, markdown: markdown.get(req.session.username) || [] });
});

app.get("/login", (req, res) => {
	if (req.session.username)
		return res.redirect("/");

	return res.render("login");
});

app.post("/login", (req, res) => {
	if (req.session.username)
		return res.redirect("/");

	const { username, password } = req.body;

	if ( username.length < 5 || username.length > 10 || typeof username !== 'string' || password.length < 8 || typeof password !== 'string' )
		return res.render("login", { err: "invalid username/password" });

	if (users.has(username)) {
		if (users.get(username) === crypto.createHash('sha256').update(password.toString()).digest('hex')) {

		} else {
			return res.render("login", { err: "invalid password" });
		}
	} else {
		users.set(username, crypto.createHash('sha256').update(password.toString()).digest('hex'));
		req.session.username = username;

		return res.redirect("/");
	}
});

app.all("/logout", (req, res) => {
	req.session.destroy();
	return res.redirect("/login")
});

app.post("/generate", (req, res) => {
	if (!req.session.username)
		return res.redirect("/");

	const username = req.session.username;
	const { title, html } = req.body;

	if (!title || typeof title !== 'string' || title.length > 20) {
		return res.redirect("/");
	}
	if (!html || typeof html !== 'string' || html.length > 1000) {
		return res.redirect("/");
	}

	const generated_markdown = Turndown.turndown(html);
	const is_shared = false;
	const uid = '';

	const user_markdown = markdown.get(username) || [];
	user_markdown.push({
		title,
		html,
		generated_markdown,
		username,
		is_shared,
		uid
	});
	markdown.set(req.session.username, user_markdown);

	return res.redirect('/');
});

app.get("/read/:id", (req, res) => {
	if (!req.session.username)
		return res.redirect("/");

	const { id } = req.params;
	if(!/^\d+$/.test(id))
        return res.redirect("/");

	const user_markdown = markdown.get(req.session.username);
	const found = user_markdown && user_markdown[id];

	if (found)
		return res.render("read", { id: id, title: found.title, markdown: found.generated_markdown });
	else
		return res.redirect("/");
});

app.get("/share/:id", (req, res) => {
	if (!req.session.username)
		return res.redirect("/");

	const { id } = req.params;
	if(!/^\d+$/.test(id))
		return res.redirect("/");

	const user_markdown = markdown.get(req.session.username);
	const found = user_markdown && user_markdown[id];

	if (found) {
		if (found.is_shared) {
			return res.redirect("/share/read/"+found.uid);
		}
		const uid = uuid();
		shared_markdown.set(uid, found);
		found.is_shared = true;
		found.uid = uid;
		return res.redirect("/share/read/"+uid);
	} else {
		return res.redirect("/");
	}
});

app.get("/share/read/:uid", (req, res) => {
	const { uid } = req.params;
	if(!/^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$/.test(uid))
		return res.redirect("/");

	const found = shared_markdown.get(uid);
	if (found) {
		return res.render("share", { uid: found.uid, title: found.title, markdown: found.generated_markdown, username: found.username });
	} else {
		return res.redirect("/");
	}
});

app.get("/report/:uid", (req, res) => {
	if (!req.session.username)
		return res.redirect("/");

	const { uid } = req.params;
	const username = req.query.username;

	if(!/^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$/.test(uid))
		return res.redirect("/");

	const found = shared_markdown.get(uid);
	if (!found) {
		return res.redirect("/");
	}
	
	try {
		if (report.has(username) && report.get(username) + 30 > now()) {
			return res.render("report", { msg: "too fast" });
		}
		report.set(username, now());
		visit(uid);
		return res.render("report", { msg: "done" });
	} catch {
		return res.render("report", { msg: "failed" });
	}

	return res.redirect("/");
});

app.listen(8000, function() {
    console.log("Server started.");
});
