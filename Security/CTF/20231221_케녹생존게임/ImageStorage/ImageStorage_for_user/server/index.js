const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 9000;
app.use(cors());

app.use(express.json());

app.use('/signup', require('./routes/signup'));

app.use('/login', require('./routes/login'));

app.use('/', require('./routes/getImage'));

app.use('/admin', require('./routes/admin'));

app.listen(PORT, () => {
});
