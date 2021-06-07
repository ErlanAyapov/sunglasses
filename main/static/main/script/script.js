function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function InputR() {
    var rng = document.getElementById('r1');
    var p = document.getElementById('one');
    p.innerHTML = rng.value;
}


function CheckBox1() {
    var id_product;
    id_product = document.getElementsByName('product');
    // id_product = document.getElementsByClassName('form-check-input');
    var buy;
    buy = document.getElementById('buy');

    // if (id_product.checked) {
    //     buy.style.display = 'block'
    // }
    for(var i=0; i < id_product.length; i++) {
        if (id_product[i].checked) {
            buy.style.display = 'block'
        }
        // else {
        //     buy.style.display = 'none'
        // }
    };
    
}