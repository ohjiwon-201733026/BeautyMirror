module.exports=function(app){
  //메인페이지
  app.get('/',function(req,res){
    res.render('index.html')
  });

  //색깔 출력 페이지 test
  app.get('/printcolors',function(req,res){
    res.render('printcolors.html');
  });

//이렇게 하면 다음페이지에서 배열로 표시됨
//ex) ["choice5","choice7","choice8"]

  app.get('/choice_result',function(req,res){
    //res.send(req.query.bestColor);
    //여기서 res.router로 새로운페이지(3개의 천슬라이드를 가진 페이지를 import해주면 그 페이지로 넘어갈 듯하다.)
    var array=[];
    array=req.query.bestColor;
    console.log(array[0]);
    console.log(array[1]);
    console.log(array[2]);
    res.render('new.html');//됏당..
    console.log('new page');
  })


}
