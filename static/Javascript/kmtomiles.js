// Function for radius conversion
function fun_radius($str, $str1, $val) {
    var datass = document.getElementById($str1).innerHTML;
    var xx = parseInt(datass);
    var change_value = 0;
    if ($str == 'Kilometer')
        change_value = $val;
    else
        change_value = Math.round(($val / 1.60934) * 100) / 100;

    document.getElementById($str1).innerHTML = change_value;
}