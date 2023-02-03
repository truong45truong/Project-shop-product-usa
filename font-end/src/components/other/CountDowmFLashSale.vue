<template>
    <div class="d-flex">
        <div class="timer" id="timer-date">
            <p class="text-white m-0 ms-1 time-show-sec"> {{date_prop}} </p>
        </div>
        <p class="text-white m-0 ms-1 time-show"> : </p>
        <div class="timer" id="timer-hour">
            <p class="text-white m-0 ms-1 time-show"> {{hour_prop}} </p>
        </div>
        <p class="text-white m-0 ms-1 time-show"> : </p>
        <div class="timer" id="timer-min">
            <p class="text-white m-0 ms-1 time-show"> {{mins_prop}} </p>
        </div>
        <p class="text-white m-0 ms-1 time-show"> : </p>
        <div class="timer" id="timer-sec">
            <p class="text-white m-0 ms-1 time-show"> {{secs_prop}} </p>
        </div>
    </div>
</template>
  
<script>

export default ({
    name: 'CountDownFLashSale',
    props: {
        hour_deadline : new Date("2023-02-03T17:30:00"),
        date_prop : '',
        hour_prop : '',
        mins_prop : '',
        secs_prop : '', 
    },
    data: () => ({
        date : 0 ,
        hour : 0 ,
        mins : 0 ,
        secs : 0 ,
        isFinish : false,
    }),
    methods : {
    },
    mounted (){
        this.date = this.date_prop
        this.hour = this.hour_prop
        this.mins = this.mins_prop
        this.secs = this.secs_prop
    },
    created(){
        let time = new Date("2023-02-03T17:30:00");
        setInterval(() => {
            const currentTime = new Date();
            let day = time.getDate()
            let h = time.getHours()
            let min = time.getMinutes();
            let sec = time.getSeconds();
            if(sec <  currentTime.getSeconds() ){
                min = min - 1 ;
                sec = sec + 60
            }
            sec = sec - currentTime.getSeconds()
            if( min <  currentTime.getMinutes()  ){
                h = h-1;
                min = min + 60
            }
            min = min - currentTime.getMinutes()
            if( h < currentTime.getHours()){
                day = day - 1
                h = h+60
            }
            h = h - currentTime.getHours()
            if ( day < currentTime.getDate){
                this.isFinish = true;
            }

            let timer_sec = document.getElementById('timer-sec')
            let p_sec = document.createElement("p")
            p_sec.setAttribute('class','text-white m-0 ms-1 time-show-sec')
            if(sec < 10){
                p_sec.innerText = "0"+sec
            } else {
                p_sec.innerText = sec
            }

            timer_sec.innerContent = ''
            timer_sec.appendChild(p_sec)
            timer_sec.removeChild(timer_sec.firstChild);
            if(this.mins != min ){
                let timer_min = document.getElementById('timer-min')
                let p_min = document.createElement("p")
                p_min.setAttribute('class','text-white m-0 ms-1 time-show')
                if(min < 10){
                    p_min.innerText = "0"+min
                } else  {
                    p_min.innerText = min ;
                }
                timer_min.innerContent = ''
                timer_min.appendChild(p_min)
                timer_min.removeChild(timer_min.firstChild);
                this.mins = min;
            }
            if(this.hour != h) {
                let timer_hour = document.getElementById('timer-hour')
                let p_hour = document.createElement("p")
                p_hour.setAttribute('class','text-white m-0 ms-1 time-show')
                p_hour.innerText = h
                timer_hour.innerContent = ''
                timer_hour.appendChild(p_hour)
                timer_hour.removeChild(timer_hour.firstChild);
                this.hour = h;
            }
            if(this.date != day ){
                let timer_day = document.getElementById('timer-date')
                let p_day = document.createElement("p")
                p_day.setAttribute('class','text-white m-0 ms-1 time-show')
                p_day.innerText = day
                timer_day.innerContent = ''
                timer_day.appendChild(p_day)
                timer_day.removeChild(timer_day.firstChild);   
                this.date= day; 
            }
        }, 1000);
    }
    
})
</script>
<style>
@keyframes showTimeCountDownSec {
    0% {
        top:-100%;
    }
    50% {top:0%;}
    100% {
        top:100%;
    }
}
@keyframes showTimeCountDown {
    from {
        top:0%;
    }
    to {top:100%;}
}
@keyframes showTimeCountUp {
    from {
        top:-100%;
    }
    to {top:0%;}
}
.timer{
    position: relative;
    overflow-y: hidden;
}
.time-show-sec {
    position:relative;
    padding : 5px 10px;
    background-color: brown;
    animation: showTimeCountDownSec 1s;
}

.time-show::before {
    background-color: brown;
}

.time-show{
    position:relative;
    padding : 5px 10px;
    background-color: brown;
    animation: showTimeCountDown 0.5s,showTimeCountUp 1s;
}
</style>