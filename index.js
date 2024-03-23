const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const app = express();
const student = require('./schema/studentSchema')
const QRCode = require('qrcode');
const usetube = require('usetube')
const {spawn}  = require('child_process');
const _ = require('lodash');
const fs = require('fs');
const jsonData = fs.readFileSync('./interest.json', 'utf8');
const recommendations = JSON.parse(jsonData);

const mongourl = "";
const conneectdb = async () =>{
  await mongoose.connect(mongourl);
  console.log('connectedd to db');
  
}
conneectdb();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


app.get('/', async (req, res) => {
    res.render('home',{marks});
  });

  app.get('/students', async(req, res) => {

    const students = await student.find();
    res.render('students',{students});
  });
  app.get('/forms', (req, res) => {
    res.render('forms');
  });
  
  app.get('/stats' ,async(req,res) =>{
    res.render('comaparing')
  })
  app.post("/stats", async (req, res) => {
    let rollno1 = req.body.entry1;
    let rollno2 = req.body.entry2;
    let studentboi1 = await student.findOne({rollno: rollno1.toUpperCase()});
    let studentboi2 = await student.findOne({rollno: rollno2.toUpperCase()});
    res.render('stats', {studentboi1,studentboi2})
  });
  
  app.get('/test' ,async(req,res) =>{
    res.render('test')
  })
  
  app.get('/newstudent' ,async(req,res) =>{
    res.render('newstudent')
  })

  app.post('/newstudent', async (req,res) => {
    let domain = req.body.domain
    let project = req.body.project
    let python =  req.body.pythonRadio
    let sql =  req.body.mysqlRadio
    let java =  req.body.javaRadio

    const qualitativeToNumeric = {
      'Strong': 2,
      'Average': 1,
      'Weak': 0,
    };
    // 
  const numericValuePY = qualitativeToNumeric[python];
  const numericValueSQL = qualitativeToNumeric[sql];
  const numericValueJAVA = qualitativeToNumeric[java];
  
    const pythonProcess = spawn('python', ['forest.py', domain, project, numericValuePY, numericValueSQL,numericValueJAVA]);
    pythonProcess.stdout.on('data', async(data) => {
      let d = data.toString('utf8')
      const vrDeveloperRecommendations = await recommendations.filter((recommendation) => recommendation.interest === d.trim());
      const recommned = vrDeveloperRecommendations[0];
      console.log(recommned)

      const genvideos = await usetube.searchVideo(`${data} roadmap`);
      let videostosent = genvideos.videos
      return res.render('recommendations',{videostosent, data, recommned});
    }
  );
  pythonProcess.on('close', (code) => {
    console.log(`Python Script Exited with Code ${code}`);});
  
  })

  app.get('/students/:name', async(req, res) => {
    var name = req.params.name;
    let studentboi = await student.findOne({name});
    if(name == "elvish bhai"){
      res.render('elvish');
    }
    else if(!studentboi){
        res.send(`No data available`)
    }else{
        res.render('viewstudent', {studentboi})
  
    }
  });


app.listen( 5000, () => {
    console.log(`Server is running on http://localhost:5000`);
  });
  
