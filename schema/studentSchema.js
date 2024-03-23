const mongoose = require('mongoose')

const userProfile = mongoose.Schema({
    name: String,
    rollno: String,
    ssc: Number,
    diploma: Number,
    dwm: Number,
    cn: Number,
    wc:Number,
    ai: Number,
    statat:Number,
    qrlink: String,
    sem3: Number,
    sem4: Number,
    future: String,
});
module.exports = mongoose.model('Profile', userProfile, 'profile');