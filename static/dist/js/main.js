$(document).ready(function () {
    $('.transparent-btn2').click(function () {
        $('.page-1').css('display', 'none');
        $('.page-2').css('display', 'block')
    });
    $('.transparent-btn3').click(function () {
        $('.page-2').css('display', 'none');
        $('.page-3').css('display', 'block')
    });
    $('.transparent-btn4').click(function () {
        $('.page-3').css('display', 'none');
        $('.page-1').css('display', 'block')
    });
    $('.transparent-btn1').click(function () {
        $('.game').css('display', 'block');
        init();
    });
    $('.onemore').click(function () {
        location.reload()
    })

});