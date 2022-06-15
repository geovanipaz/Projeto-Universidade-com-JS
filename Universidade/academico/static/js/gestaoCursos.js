(function (){
    const btnEliminacao = document.querySelectorAll(".btnEliminacao");

    btnEliminacao.forEach(btn =>{
        btn.addEventListener('click',(e) =>{
            const confimacao = confirm('Quer mesmo eliminar o curso?');
            if(!confimacao){
                e.preventDefault();
            }
        })
    })
})();

