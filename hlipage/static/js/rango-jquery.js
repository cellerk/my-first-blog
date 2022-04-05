$(document).ready(function() {

    $('#check_all').click(function() {
        $('input[name=or_choose_which_author]').prop('checked', true);
    });

    $('#uncheck_all').click(function() {
        $('input[name=or_choose_which_author]').prop('checked', false);
    });

});