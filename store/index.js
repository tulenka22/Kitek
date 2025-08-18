import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const state = () => ({
  blindMode: false,
  specialties: [],
})

export const actions = {}

export const mutations = {
  setSpecialties(state, value) {
    state.specialties = value
  },
}

export const getters = {}
