function errorSeeProf(){
    swal.fire({
        icon: 'error',
        title: 'خطا',
        text: 'لطفا وارد شوید',
        footer: '<a href="login.html">وارد شوید</a>',
        color: '#00adb5'
    })
}

function More(){
  const about = [`<div><br><p>نام : اژدر</p><br><br><p>ایمیل : ajdar@gmail.com</p></div><br><br><br><br><a style="color: #00adb5; cursor: pointer;" onclick="more()"><<</a>`]
const more = document.getElementById('more')
  more.innerHTML = about
}

function more(){
  const again = [`<br><br><br><br><br><br><br><br><a onclick="More()"><h3 style="color: #00adb5; cursor: pointer;">>></h3></a>`]
  const more = document.getElementById('more')
  more.innerHTML = again
}

function popUp(){
const stone = [`<div style=" background-color: #222831; width: 350px; height: 560px;color: azure; border-radius: 10px; box-shadow: 2px 3px 10px  #16181b; margin-top: -10px; margin-right: 74%; position: absolute;"><br><p style="text-align: center; float: right; margin-right: 30px; background-color: red; width: 100px; border-radius: 20px; cursor: pointer;" onclick="closed()">بستن</p><br><br><div style="text-align: right; float: right;"><img src="picture/prof.png" alt="profile" style="text-align: right; width: 50px;border-radius: 2000px; padding: 3px;background-color: lightgreen; margin-right: 10px; margin-top: 8px;"></div><div style="float: right; margin-right: 10px; margin-top: -10px; text-align: right;"><p style="margin: 16px; text-align: right; font-size: 25px;">آرشا کیقبادی</p><p style="font-size: 15px; margin: 13px; text-align: right;">arsha.keighobadi.88@gmail.com</p></div><br><hr style="display: block; width: 300px;margin: 23px; color: #222831;"><div style="width: 20px; height: 20px; text-align: center; float: right; margin: 15px; background-color: #00ADB5; border-radius: 50px;"><p style="color: #00adb5;">.</p></div><p style="float: right; margin-right: 15px; width: 250px; padding-top: 15px;" class="pop">موجودی کیف پول</p><br><br><br><div style="width: 20px; height: 20px; text-align: center; float: right; margin: 15px; background-color: #006368; border-radius: 50px;"><p style="color: #006368;">.</p></div><p style="float: right; margin-right: 15px; padding-top: 15px; width: 250px;" class="pop">امتیاز</p><br><br><br><div style="width: 20px; height: 20px; text-align: center; float: right; margin: 15px; background-color: #003c3f; border-radius: 50px;"><p style="color: #003c3f;">.</p></div><p style="float: right; margin-right: 15px; width: 250px; padding-top: 15px;" class="pop">تعداد دوره های ثبت نام شده</p><br><br><br><hr style="display: block; width: 300px;margin: 23px; color: #222831;"><div style="float: right; text-align: right;  padding-right: 20px; margin-right: 20px; "><p>خرید اشتراک</p><br><p>سوالات</p></div><br><br><br><hr style="display: block; width: 300px;margin: 23px; color: #222831;"><div style="float: right; padding-right: 25px; font-size: 25px;"><p style="color: red;"class="pop" >خروج</p></div></div>`]
const popUp = document.getElementById('red')
popUp.innerHTML = stone
} 
function closed(){
  const hhh = [`<div></div>`]
  const HHH = document.getElementById('red')
  HHH.innerHTML = hhh
}