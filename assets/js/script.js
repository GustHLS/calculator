function createCalculator(){
    return{
        display: document.querySelector('.display'),


        start(){
            this.clickBtn();
        },

        clickBtn(){
            document.addEventListener('click', function(e) {
                const element = e.target;

                if(element.classList.contains('btn-num')){
                    this.btnStopDisplay(element.innerText);
                }
            }.bind(this));
        },

        btnStopDisplay(value){
            this.display.value += value;
        },
    }
}

const calculator = createCalculator();
calculator.start();