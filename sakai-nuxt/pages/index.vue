<script>
import animationData from '~/assets/animations/animation_llgzj9m2.json';
// import { states } from '../service/composables/states';
// import { useMainStore } from '../service/composables/userstore';
import { useMainStore } from '../service/composables/userstore';
export default {
    name: 'App',
    data() {
        return {
            windowWidth: 0,
            animationData: animationData
        };
    },
    mounted() {
        // useMainStore().set_jwt(localStorage.getItem('jwt_token'));
        // useMainStore().set_email(localStorage.getItem('email'));
        // Initialize window dimensions on component creation
        this.windowWidth = window.innerWidth;
        // Add a listener to update dimensions when window is resized
        window.addEventListener('resize', this.setWindowSize);
    },
    unmounted() {
        // window.removeEventListener('resize', this.setWindowSize);
    },
    methods: {
        setWindowSize() {
            // states.set_window_width(window.innerWidth);
            // console.log(states.get_window_width().value);
            this.windowWidth = window.innerWidth;
        }
    }
};
</script>

<template>
    <AdvantageBanner></AdvantageBanner>
    <Animation :animationData="animationData" class="responsive-animation" v-if="windowWidth < 982"></Animation>
    <FlexRow cross-axis-alignment="center" main-axis-alignment="center" style="margin-bottom: 10%"
        ><FlexColumn>
            <div style="font-size: 3.5dvh" class="text-900 mb-3 font-medium">KAZAI - алғашқы қазақша AI ассистент</div>
            <div style="font-size: 2dvh" class="text-blue-600 mb-3 font-medium">Сұрағыңызға небәрі 5 секундта жауап алыңыз😉</div>
            <FlexRow>
                <router-link to="/conversation"><Button label="KAZAI" icon="pi pi-send" raised size="large" /></router-link>
                <router-link to="/history"><Button label="Тарих" icon="pi pi-clock" raised outlined size="large" style="margin-left: 20%" /></router-link>
            </FlexRow>
        </FlexColumn>
        <Animation :animationData="animationData" style="height: 40%; width: 40%; color: blue" v-if="windowWidth >= 982"></Animation
    ></FlexRow>
    <Examples></Examples>
    <FAQ style="margin-left: 17%; margin-bottom: 3%"></FAQ>
</template>

<style scoped>
.responsive-animation {
    max-width: 100%; /* Make sure the animation doesn't exceed its container */
    width: auto; /* Allow the width to adjust based on container size */
    height: auto; /* Allow the height to adjust based on container size */
    color: blue; /* You can keep your color styling here */
}
</style>
