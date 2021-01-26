$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;



	$('#user_name').blur(function() {
		check_user_name();

	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名')
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			  /*获取XMLRequest的对象，可以发送异步请求*/
            var xmlhttp;
            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            } else {
                xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
            }
            /*绑定事件*/
            xmlhttp.onreadystatechange = function () {

                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    if (xmlhttp.responseText == '1') {
                    	// alert(1)
                        $('#user_name').next().html('用户名已经存在')
                        $('#user_name').next().show();
                        error_name = true;

                    } else {
                    	// alert(2)
                        $('#user_name').next().show();
                        $('#user_name').next().html('ok')
                        error_name = false;

                    }
                }
            }
            /*准备并发送*/
            xmlhttp.open('get', '/fruist/checkusername?user_name=' + user_name.value, true)
            xmlhttp.send()


		}
	}





	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<3||len>20)
		{
			$('#pwd').next().html('密码最少3位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{	$('#pwd').next().html('ok')
			$('#pwd').next().show();
			error_password = false;
		}
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			// $('#cpwd').next().html('ok')
			error_check_password = false;
		}

	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('.reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});








})