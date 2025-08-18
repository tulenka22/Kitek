<template>
  <block-ab title="График учебного процесса">
      <div class="cont-text">
        <h2 class="ab__subtitle"><b red>Расписание звонков для студентов 1 и 2 курса</b></h2>
        <p class="ab__p">
          <b>Расписание звонков по понедельникам:</b>
          <ul>
            <li>
              <b>1 пара.</b> 8:45 - 10:15
            </li>
            <li>
              <b>Кураторский час</b> 10:25 - 10:55
            </li>
            <li>
              <b>2 пара.</b> 11:05 - 11:50
            </li>
            <li>
              <b> Перерыв для 1 и 2 курса.</b> 35 мин
            </li>
            <li>
              <b>2 пара.</b> 12:25 - 13:10
            </li>
            <li>
              <b>3 пара.</b> 13:20 - 14:50
            </li>
            <li>
              <b>4 пара.</b> 15:00 - 16:30
            </li>
            <li>
              <b>5 пара.</b> 16:40 - 18:10
            </li>
            <li>
              <b>6 пара.</b> 18:15 - 19:45
            </li>
          </ul>
        </p>
        <p class="ab__p">
          <b>Расписание звонков:</b>
          <ul>
            <li>
              <b>1 пара.</b> 8:45 - 10:15
            </li>
            <li>
              <b>2 пара.</b> 10:25 - 11:10
            </li>
            <li>
              <b> Перерыв для 1 и 2 курса.</b> 30 мин
            </li>
            <li>
              <b>2 пара.</b> 11:40 - 12:25
            </li>
            <li>
              <b>3 пара.</b> 12:35 - 14:05
            </li>
            <li>
              <b>4 пара.</b> 14:15 - 15:45
            </li>
            <li>
              <b>5 пара.</b> 15:55 - 17:25
            </li>
            <li>
              <b>6 пара.</b> 17:30 - 19:00
            </li>
          </ul>
        </p>
      </div>

      <div class="cont-text">
        <h2 class="ab__subtitle"><b red>Расписание звонков для студентов 3 и 4 курса</b></h2>
        <p class="ab__p">
          <b>Расписание звонков по понедельникам:</b>
          <ul>
            <li>
              <b>1 пара.</b> 8:45 - 10:15
            </li>
            <li>
              <b>Кураторский час</b> 10:25 - 10:55
            </li>
            <li>
              <b>2 пара.</b> 11:05 - 12:35
            </li>
            <li>
              <b> Перерыв для 3 и 4 курса.</b> 45 мин
            </li>
            <li>
              <b>3 пара.</b> 13:20 - 14:50
            </li>
            <li>
              <b>4 пара.</b> 15:00 - 16:30
            </li>
            <li>
              <b>5 пара.</b> 16:40 - 18:10
            </li>
            <li>
              <b>6 пара.</b> 18:15 - 19:45
            </li>
          </ul>
        </p>
        <p class="ab__p">
          <b>Расписание звонков:</b>
          <ul>
            <li>
              <b>1 пара.</b> 8:45 - 10:15
            </li>
            <li>
              <b>2 пара.</b> 10:25 - 11:55
            </li>
            <li>
              <b> Перерыв для 3 и 4 курса.</b> 40 мин
            </li>
            <li>
              <b>3 пара.</b> 12:35 - 14:05
            </li>
            <li>
              <b>4 пара.</b> 14:15 - 15:45
            </li>
            <li>
              <b>5 пара.</b> 15:55 - 17:25
            </li>
            <li>
              <b>6 пара.</b> 17:30 - 19:00
            </li>
            <li>
              <b>7 пара.</b> 19:05 - 20:35
            </li>
          </ul>
        </p>
      </div>
      <div>
        <p class="ab__p"><b red>ГРАФИК УЧЕБНОГО ПРОЦЕССА:</b></p>
        <ul class="ab__list" v-for="spec in specialtes" :key="spec.eduprocess">
          <a :href="spec.eduprocess" target="_blank" class="ab__p ab__link">{{ spec.name}} </a>
        </ul>
      </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  data() {
    return {
      specialtes: [],
    }
  },
  async created() {
    try {
      this.specialtes = JSON.parse(await loadDynamic('dynamic/specs/specs.json'))
    }
    catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
}
</script>

<style scoped lang="scss">

.cont-text{
  float: left;
  margin-top: 20px;
  margin-right: 50px;
  height: 550px;
  @include high-medium-media {
      float: none
    }
}

</style>
