$(function () {
    var myDate=new Date();
    //获取年份
    var fy=myDate.getFullYear();
    //获取月份
    var mt=myDate.getMonth()+1;
    //获取日期
    var dt=myDate.getDate();
    $("#year").text(fy+"-"+mt+"-"+dt);
})