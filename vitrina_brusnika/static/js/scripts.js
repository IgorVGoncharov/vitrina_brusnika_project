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
