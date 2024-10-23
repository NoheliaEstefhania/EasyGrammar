<template>
  <div class="">
    <div class="flex flex-col gap-3 mb-9">
      <h2 class="text-xl font-medium">Generar Ejemplo</h2>
      <div class="flex gap-4">
        <input class="rounded-xl p-2" type="text" placeholder="Escribe algo" />
        <button @click="genSentence"
          class="p-2 border-2 rounded-xl bg-tertiary border-tertiary text-white transition-transform duration-200 active:translate-y-[-10px]">
          <p>Generar</p>
        </button>
      </div>
    </div>

    <div class="grid grid-cols-4 grid-rows-4 gap-2">
    
      <div v-if="genlvl_0" class="col-span-3 border-4 rounded-lg border-white px-3 py-1">
        <p>{{sentenceSelect.oracion}}</p>
      </div>
     

      <div v-if="showlvl_1" class="row-start-2 col-span-1 border-4 rounded-lg border-[#60BFB2]  px-3 py-1">
        <p>{{sentenceSelect.sujeto.completo}}</p>
      </div>
      <div v-if="showlvl_1" class="row-start-2 col-span-2 border-4 rounded-lg border-[#FF7B4D] px-3 py-1">
        <p>{{sentenceSelect.predicado.completo}}</p>
      </div>

     
      <div v-if="showlvl_2" class="row-start-3 col-span-1 border-4 rounded-lg border-[#60BFB2]  px-3 py-1">
        <p>{{sentenceSelect.sujeto.sustantivo}}</p>
      </div>
      <div v-if="showlvl_2" class="row-start-3 col-span-1 border-4 rounded-lg border-[#E19B00]  px-3 py-1">
        <p>{{sentenceSelect.predicado.verbo.completo}}</p>
      </div>
      <div v-if="showlvl_2" class="row-start-3 col-span-1 border-4 rounded-lg border-[#FFD966] px-3 py-1">
        <p>{{sentenceSelect.predicado.complemento}}</p>
      </div>
      <div v-if="showlvl_3" class="row-start-4 col-start-2 flex flex-row gap-2">
        <div class="border-4 rounded-lg border-[#FF7B4D] px-3 py-1 flex-1">
          <p >{{sentenceSelect.predicado.verbo.radical}}</p>
        </div>
        <div class="border-4 rounded-lg border-[#E75F09] px-3 py-1 flex-1">
          <p >{{sentenceSelect.predicado.verbo.desinencia}}</p>
        </div>
      </div>
      <div class="col-start-4  row-start-2 flex justify-center">
        <button @click="showDivs_1" v-if="genlvl_0"
          class="w-24 border-2 border-black rounded-xl bg-[#FFD966] transition-transform duration-200 active:translate-y-[-10px]">
          Nivel 1
        </button>
      </div>
      <div class="col-start-4 row-start-3 flex justify-center">
        <button @click="showDivs_2" v-if="genlvl_0 && showlvl_1"
          class="w-24 border-2 border-black rounded-xl bg-[#FFB54A] transition-transform duration-200 active:translate-y-[-10px]">
          Nivel 2
        </button>
      </div>
      <div class="col-start-4 row-start-4 flex justify-center">
        <button @click="showDivs_3"  v-if="genlvl_0 && showlvl_1 && showlvl_2"
          class="w-24 border-2 border-black rounded-xl bg-[#FF7B4D] transition-transform duration-200 active:translate-y-[-10px]">
          Nivel 3
        </button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { reactive } from 'vue';

const showlvl_1 = ref(false)
const showlvl_2 = ref(false)
const showlvl_3 = ref(false)
const genlvl_0 = ref("")


let sentenceSelect = reactive({})


const sentences2 = [
  {
    oracion: "El perro corre por el parque",
    sujeto: {
      completo: "El perro",
      sustantivo: "perro"
    },
    predicado:{
      completo:"corre por el parque",
      verbo: {
        completo: "corre",
        radical: "corr",
        desinencia: "e"
      },
      complemento: "por el parque"
    }
  },
  {
    oracion: "María estudia para el examen",
    sujeto: {
      completo: "María",
      sustantivo: "María"
    },
    predicado: {
      completo: "estudia para el examen",
      verbo: {
        completo: "estudia",
        radical: "estudi",
        desinencia: "a"
      },
      complemento: "para el examen"
    }
  },
  {
    oracion: "Los pájaros cantan al amanecer",
    sujeto: {
      completo: "Los pájaros",
      sustantivo: "pájaros"
    },
    predicado: {
      completo: "cantan al amanecer",
      verbo: {
        completo: "cantan",
        radical: "cant",
        desinencia: "an"
      },
      complemento: "al amanecer"
    }
  },
  {
    oracion: "Mi hermano juega fútbol los fines de semana",
    sujeto: {
      completo: "Mi hermano",
      sustantivo: "hermano"
    },
    predicado: {
      completo: "juega fútbol los fines de semana",
      verbo: {
        completo: "juega",
        radical: "jug",
        desinencia: "a"
      },
      complemento: "fútbol los fines de semana"
    }
  },
  {
    oracion: "El profesor explica la lección con claridad",
    sujeto: {
      completo: "El profesor",
      sustantivo: "profesor"
    },
    predicado: {
      completo: "explica la lección con claridad",
      verbo: {
        completo: "explica",
        radical: "explic",
        desinencia: "a"
      },
      complemento: "la lección con claridad"
    }
  },
  {
    oracion: "Las flores crecen en el jardín",
    sujeto: {
      completo: "Las flores",
      sustantivo: "flores"
    },
    predicado: {
      completo: "crecen en el jardín",
      verbo: {
        completo: "crecen",
        radical: "crec",
        desinencia: "en"
      },
      complemento: "en el jardín"
    }
  },
  {
    oracion: "Pedro y Ana viajan a la playa cada verano",
    sujeto: {
      completo: "Pedro y Ana",
      sustantivo: "Pedro y Ana"
    },
    predicado: {
      completo: "viajan a la playa cada verano",
      verbo: {
        completo: "viajan",
        radical: "viaj",
        desinencia: "an"
      },
      complemento: "a la playa cada verano"
    }
  }
];


const genSentence = ()=>{
  const random = Math.floor(Math.random()*sentences2.length);
  sentenceSelect = sentences2[random]

  genlvl_0.value =  sentenceSelect
  showlvl_1.value = false
  showlvl_2.value = false
  showlvl_3.value = false

}

const showDivs_1 = () =>{
  showlvl_1.value = !showlvl_1.value;
}
const showDivs_2 = () =>{
  showlvl_2.value =  !showlvl_2.value;
}
const showDivs_3 = () =>{
  showlvl_3.value =  !showlvl_3.value;
}





</script>

<style scoped></style>
