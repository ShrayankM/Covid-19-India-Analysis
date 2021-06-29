var stateName = "";
var temp = ""
var stateINFO = {}

function strip(str) {
    return str.replace(/^\s+|\s+$/g, '');
}
storeData()

$( "#state_select" ).change(function () {
    var str = "";
    $( "#state_select option:selected" ).each(function() {
      str += $(this).text();
    });
    var temp = strip(str)
    var state_details = String(stateINFO[temp])
    state_details = state_details.split(',')
    $('#confirm').text(new Intl.NumberFormat('en-IN').format(state_details[0]).concat('\u2191'));
    $('#recover').text(new Intl.NumberFormat('en-IN').format(state_details[1]).concat('\u2191'))
    $('#decease').text(new Intl.NumberFormat('en-IN').format(state_details[2]).concat('\u2191'))

    $('#tc').text(new Intl.NumberFormat('en-IN').format(state_details[3]))
    $('#tr').text(new Intl.NumberFormat('en-IN').format(state_details[4]))
    $('#td').text(new Intl.NumberFormat('en-IN').format(state_details[5]))

  }).change();

function storeData(){
    var states = $('#state_hidden option');
    for(var i = 0; i < states.length; i++){
        state_split = states[i].text.split(' ')
        var index = state_split.length - 7;
        var str = ""
        str += state_split[0]
        for(var j = 1; j <= index; j++)
            str += " " + state_split[j];
        L = [];
        for(var j = state_split.length - 1; j >= state_split.length - 6; j--)
            L.push(state_split[j]);
        stateINFO[str] = L.reverse();
    }
}

const indiaDate = document.querySelector('.india__date');
const day = `${(new Date()).getDate()}`.padStart(2, '0');
const month = `${(new Date()).getMonth() + 1}`.padStart(2, '0');
const year = (new Date()).getFullYear();

// console.log(day, month, year);
indiaDate.textContent = `${indiaDate.textContent} (${day}/${month}/${year})`;

const arr = document.querySelectorAll('.overall');
// console.log(arr);

arr.forEach(function(element) {
    element.innerHTML = `${new Intl.NumberFormat('en-IN').format(element.innerHTML)}`;
})


const overToday = document.querySelectorAll('.over-today');
overToday.forEach(function(element) {
    // console.log(element.innerHTML.replaceAll(' ', ''));
    const str = element.innerHTML.replaceAll(' ', '');
    element.innerHTML = `${new Intl.NumberFormat('en-IN').format(str.slice(0, -1))} ${str.slice(-1)}`;
})
