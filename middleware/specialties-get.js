import { loadDynamic } from '~/core/helpers/file'

export default async function ({ store }) {
  if (store.state.specialties.length > 0) return
  const specs = JSON.parse(await loadDynamic('dynamic/specs/specs.json'))
  store.commit('setSpecialties', specs)
}
