// window.addEventListener('popstate', function(event) {
//     // The popstate event is fired each time when the current history entry changes.

//     var r = confirm("You pressed a Back button! Are you sure?!");

//     if (r == true) {
//         // Call Back button programmatically as per user confirmation.
//         history.back();
//         // Uncomment below line to redirect to the previous page instead.
//         // window.location = document.referrer // Note: IE11 is not supporting this.
//     } else {
//         // Stay on the current page.
//         history.pushState(null, null, window.location.pathname);
//     }

//     history.pushState(null, null, window.location.pathname);

// }, false);

$(document).ready(function(){

    // ===== Scroll to Top ==== 
	$(window).scroll(function() {
	    if ($(this).scrollTop() >= 500) {        // If page is scrolled more than 500px
	        $('#return-to-top').fadeIn(200);    // Fade in the arrow
	    } else {
	        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
	    }

	    if ($(this).scrollTop() >= 500){
	    	$('.goto-back').fadeIn(200);
	    } else {
	    	$('.goto-back').fadeOut(200);
	    }
	});
	$('#return-to-top').click(function() {      // When arrow is clicked
	    $('body,html').animate({
	        scrollTop : 0                       // Scroll to top of body
	    }, 500);
	});

	$(".goto-back").click(function(){
        window.history.back();
    });

    $("#goto-back").click(function(){
        window.history.back();
    });

});