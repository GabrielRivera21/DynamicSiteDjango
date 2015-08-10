$('#accordion').on('shown.bs.collapse', function (e) {
       var id = $(e.target).prev().find("[id]")[0].id;
       navigateToElement(id);
})

function navigateToElement(id) {
    $('html, body').animate({
            scrollTop: $("#" + id).offset().top - 95
    		}, 500);
}