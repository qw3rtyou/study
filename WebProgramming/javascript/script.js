class User {
    constructor(email, birthdate) {
        this.email = email;
        this.birthdate = birthdate;
    }

    buy(item) {
        console.log(`${this.email} buys ${item.name}`);
    }

    get email() {
        return this._email;
    }

    set email(address) {
        if (address.includes('@')) {
            this._email = address;
        } else {
            throw new Error('invalid email address');
        }
    }
}

const user1 = new User('chris123@google.com', '1992-03-21');
user1.email = 'newChris123@google.com';
console.log(user1.email);