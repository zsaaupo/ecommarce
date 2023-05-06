let updateBtns = document.getElementsByClassName('update-cart')

// listener for add to cart button
for (i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log("productId:", productId, "action:", action)

        console.log(user)
        if(user === 'AnonymousUser'){
            console.log('not logged in')
        }
        else{
            console.log('User id logged in, sending data...')
        }
    })
}