// -------------------------------------
// Main.js
// -------------------------------------

// Set focus on first load
$(document).ready(function() {
    $('#search').focus();
});

// Set loading state on button if a request is sent
$(document).on('pjax:send', function() {
    $('#submit').button('loading');
})

// Empty search box and reset loading state for submit button
$(document).on('pjax:complete', function() {
    $('#submit').button('reset');
    $('#search').val('');
    $('#search').focus();
});

// Submit button listener
$('#submit').click(function(event) {
    event.preventDefault();
    var pokemon = $('#search').val();
    if (pokemon === "") {
        $('#searchBox').addClass('control-group error');
        $('#search').popover({
            content: "You need to search for something",
            trigger: 'manual',
            placement: 'bottom'
        }).popover('show').focus();

        $('#submit').button('reset');
        return false;
    }
    $.pjax({
        container: "#container",
        timeout: 2000,
        url: "../pokemon/" + pokemon
    });
});

// Define the typeahead
$('#search').typeahead({

    source: function(q, process){
        // return $.get('../ajax/typeahead/', {q: q}, function(response) {
        return $.get('../ajax/typeahead/' + q, success=function(response) {
            var data = new Array;
            $.each(response, function(index, key) {

                data.push(index + "#" + key);
            });
            return process(data);
        });
    },
    highlighter: function(item) {
        $('#searchBox').removeClass('control-group error');
        $('#search').popover('hide');
        $('#searchBox').popover('hide');
        var parts = item.split('#');
        return "<div class='typeaheadItem'><img src='../../static/img/sprites/" + parts[0] + ".png' > " + parts[1] + "</div>";
    },
    updater: function(item) {
        var parts = item.split('#');
        var pokemon = parts[1];
        $.pjax({
            container: "#container",
            timeout: 2000,
            url: "../pokemon/" + pokemon
        });
        return parts[1];
    },
    items: 5
});

// If search fails
$(document).on('pjax:error', function() {
    $('#searchBox').addClass('control-group error');
    $('#searchBox').popover({
        content: "Your search returned nothing",
        trigger: 'manual',
        placement: 'right'
    }).popover('show').focus();

    $('#submit').button('reset');
    return false;
});