document.querySelectorAll('.category').forEach(category => {
    category.addEventListener('click', function() {
        const targetId = this.getAttribute('data-target');
        const targetList = document.getElementById(targetId);

        if (targetList.classList.contains('active')) {
        targetList.classList.remove('active');
        } else {
        document.querySelectorAll('.product-list').forEach(list => {
            list.classList.remove('active');
        });
        
        targetList.classList.add('active');
        }
    });
});

document.querySelectorAll('a.clickable').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault(); 
        document.querySelectorAll('a.clickable').forEach(el => {
            el.classList.remove('active');
        });
        this.classList.add('active');
    });
});