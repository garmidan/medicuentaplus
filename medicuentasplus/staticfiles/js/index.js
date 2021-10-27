$(document).ready(main);
var contador = 1;
function main(){
	$('.menu_bar').click(function(){
		// $('nav').toggle(); 

		if(contador == 1){
			$('nav').animate({
				left: '0'
			});
			$('.col-9').hide();
			contador = 0;
		} else {
			contador = 1;
			$('.col-9').show('slow');
			$('nav').animate({
				left: '-100%'
			});
		}

	});

};