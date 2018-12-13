<?php
    $price= $_POST["price"];
    $pay= $_POST["pay"];
    $ans= $price-$pay;
    if ($ans > 0){
        echo $ans;
    }elseif ($ans < 0){
        echo "the money is short for  ", " = ", $ans;
    }else{
        echo "thank you for choosing";
    }
?>