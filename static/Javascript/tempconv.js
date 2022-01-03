// Function for temperature conversion
function fun_temperature($str, $ids, $val) {
    var change_value = 0;
    if ($str == '°C')
        change_value = $val;
    else if ($str == '°F')
        change_value = (($val * 9) / 5 + 32);
    else
        change_value = ($val + 273);

    document.getElementById($ids).innerHTML = change_value;
}