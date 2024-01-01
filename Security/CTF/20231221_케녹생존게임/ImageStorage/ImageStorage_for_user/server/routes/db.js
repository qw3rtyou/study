let users = [];

const addUser = async (username, password) => {
  users.push({ username, password });
};

const findUserByUsername = (username) => {
  return users.find(user => user.username === username);
};

const checkIfUserExists = (username) => {
  return users.some(user => user.username === username);
};

module.exports = { addUser, findUserByUsername, checkIfUserExists };
