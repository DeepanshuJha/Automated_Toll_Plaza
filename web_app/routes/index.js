const express = require('express');
const router = express.Router();
const User = require('../models/Users');
const passport = require('passport');

const { ensureAuthenticated } = require('../config/auth');

router.get('/', (req, res) => res.render('welcome'));

var user = [];

router.get('/dashboard', ensureAuthenticated, (req, res) => 
    res.render('dashboard', {
        user : req.user,
        status : req.user.status
    })
);

router.post('/dashboard', function(req, res){
    User.findByIdAndUpdate({_id: req.user._id}, {$set: { status : 1}} , function(err, result){
        if(err){
            console.log(err);
        }
        res.redirect('/dashboard')
    });
});

module.exports = router;