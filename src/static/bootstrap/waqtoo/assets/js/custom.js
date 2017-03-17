$(function() {
	var austDay = new Date();
	austDay = new Date(austDay.getFullYear(), 12, 20);
	$('#countdown').countdown({
		until : austDay,
		layout : 	'<ul>{y<}<li><div class="timer">{yn}</div><div class="timer-label">{yl}</div></li>' +
					'{y>}{o<}<li><div class="timer">{on}</div><div class="timer-label">{ol}</div></li>' + 
					'{o>}{d<}<li><div class="timer">{dn}</div><div class="timer-label">{dl}</div></li>' +
					'{d>}{h<}<li><div class="timer">{hn}</div><div class="timer-label">{hl}</div></li>' + 
					'{h>}{m<}<li><div class="timer">{mn}</div><div class="timer-label">{ml}</div></li>' +
					'{m>}{s<}<li><div class="timer">{sn}</div><div class="timer-label">{sl}</div></li>{s>}</ul>'
	});

	$('#size_button').click(function(){
		$('#size').html($(window).width() + ' x ' + $(window).height() 
			+ "   (pixels)");
	});

});
