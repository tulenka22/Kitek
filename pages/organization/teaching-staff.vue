<template>
  <block-ab title="Педагогический состав">
    <br />
    <ul>
      <li v-for="st of cmk" :key="st.group">
        <a
          :class="st.group == search ? 'ab__link active' : 'ab__link'"
          @click="search = st.group"
        >
          {{ st.name }}
        </a>
      </li>
    </ul>

    <div v-if="search">
      <div v-if="filteredTable.length === 0" style="padding: 20px; text-align: center;">
        Нет данных для этой группы
      </div>
      <div v-else class="cmktable__overflow dragscroll">
        <table class="a-table">
          <thead>
            <tr class="a-table__header">
              <th class="a-table__cell a-table__cell-head">Фамилия, имя, отчество</th>
              <th class="a-table__cell a-table__cell-head">Должность</th>
              <th class="a-table__cell a-table__cell-head">
                Уровень образования/ Наименование образовательного учреждения
              </th>
              <th class="a-table__cell a-table__cell-head">
                Наименование направления подготовки и (или) специальности
              </th>
              <th class="a-table__cell a-table__cell-head">
                Квалификация/<br />
                Ученая степень/<br />
                Ученое звание
              </th>
              <th class="a-table__cell a-table__cell-head">
                Преподаваемые предметы, дисциплины, междисциплинарные курсы
              </th>
              <th class="a-table__cell a-table__cell-head">
                Сведения о повышении квалификации и (или) профессиональной переподготовке
              </th>
              <th class="a-table__cell a-table__cell-head">Стаж общий</th>
              <th class="a-table__cell a-table__cell-head">Стаж работы по специальности</th>
              <th class="a-table__cell a-table__cell-head">
                Код и наименование специальностей, профессий, в реализации которых участвует
                педагогический работник
              </th>
            </tr>
          </thead>
          <tbody v-for="(emp, empIdx) of filteredTable" :key="empIdx">
            <tr>
              <td class="a-table__cell a-table__cell-8">
                <p class="cmktable__p">{{ emp.fio }}</p>
              </td>
              <td class="a-table__cell a-table__cell-8">
                <p class="cmktable__p">{{ emp.function }}</p>
              </td>
              <td class="a-table__cell a-table__cell-8">
                <p
                  class="cmktable__p"
                  v-for="(education, educationIdx) of emp.education"
                  :key="educationIdx"
                >
                  {{ education }}
                </p>
              </td>
              <td class="a-table__cell a-table__cell-8">
                <p class="cmktable__p" v-for="(spec, specIdx) of emp.spec" :key="specIdx">
                  {{ spec }}
                </p>
              </td>
              <td class="a-table__cell a-table__cell-8">
                <p
                  class="cmktable__p"
                  v-for="(qualification, qualificationIdx) of emp.qualification"
                  :key="qualificationIdx"
                >
                  {{ qualification }}
                </p>
              </td>
              <td class="a-table__cell a-table__cell-8">
                <ul
                  class="cmktable__list"
                  v-for="(teacher, teacherIdx) of emp.teacher"
                  :key="teacherIdx"
                >
                  <li v-if="teacherIdx < emp.if" style="font-size: 13px">
                    {{ teacher }}
                  </li>
                </ul>
                <a v-if="emp.if === 2 && emp.teacher.length > 2" class="ab__link" @click="emp.if = 999"> ▼Подробнее▼ </a>
                <a v-if="emp.if === 999" class="ab__link" @click="emp.if = 2"> ▲Свернуть▲ </a>
              </td>
              <td class="a-table__cell a-table__cell-8">
                <div v-for="(raise, raiseIdx) of emp.raise" :key="raiseIdx">
                  <p v-if="raiseIdx <= emp.ifr" class="cmktable__p" v-html="raise" />
                </div>
                <a v-if="emp.ifr === 1 && emp.raise.length > 2" class="ab__link" @click="emp.ifr = 999"> ▼Подробнее▼ </a>
                <a v-if="emp.ifr === 999" class="ab__link" @click="emp.ifr = 1"> ▲Свернуть▲ </a>
              </td>
              <td class="a-table__cell a-table__cell-8">
                {{ emp.general }}
              </td>
              <td class="a-table__cell a-table__cell-8">
                {{ emp.specialty }}
              </td>
              <td class="a-table__cell a-table__cell-8">
                <ul class="cmktable__list" v-for="(code, codeIdx) of emp.code" :key="codeIdx">
                  <li v-if="codeIdx < emp.ifc" style="font-size: 13px">
                    {{ code }}
                  </li>
                </ul>
                <a v-if="emp.ifc === 2 && emp.code.length > 2" class="ab__link" @click="emp.ifc = 999"> ▼Подробнее▼ </a>
                <a v-if="emp.ifc === 999" class="ab__link" @click="emp.ifc = 2"> ▲Свернуть▲ </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'

export default {
  data() {
    return {
      cmk: [
        { name: 'ЦМК Общеобразовательных дисциплин', group: 'naturalScience' },
        { name: 'ЦМК Физической культуры, БЖД и туризма', group: 'FK_BJD' },
        { name: 'ЦМК Информационных технологий и права', group: 'IT' },
        { name: 'ЦМК Технологий водного транспорта', group: 'WTT' },
        { name: 'ЦМК Экономики и бухгалтерского учета', group: 'econom' },
        { name: 'ЦМК Торгового дела', group: 'merchandiser' },
        { name: 'ЦМК Поварского и кондитерского дела', group: 'cook' },
      ],
      employeers: [],
      search: 'naturalScience',
      jsonPath: 'documents/cmk.json',
      error: 'Загрузка...',
    }
  },
  async created() {
    try {
      const documentsObj = JSON.parse(await loadDynamic(this.jsonPath))
      this.employeers = documentsObj.cmk
      console.log('✅ Загружено сотрудников:', this.employeers.length)
    } catch (err) {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}': ${err.message}`
      console.error(this.error)
    }
  },
  computed: {
    filteredTable() {
      return this.employeers.filter((emp) => emp.idgroup === this.search)
    },
    groupStats() {
      const stats = {}
      this.employeers.forEach(emp => {
        stats[emp.idgroup] = (stats[emp.idgroup] || 0) + 1
      })
      return stats
    }
  },
}
</script>

<style scoped lang="scss">
.cmktable {
  &__overflow {
    text-align: left;
    max-width: 100vw;
    overflow: auto;
    @include scrollbar();
  }
  &__p {
    margin-top: 12px;
    max-width: 1000px;
    font-size: 12px;
    text-align: left;
    @extend %tg-ab-text;
    hyphens: auto;
    @include high-media() {
      hyphens: none;
    }
    @include medium-media() {
      font-size: 14px;
    }
  }
  &__list {
    text-align: left;
    margin-top: 14px;
    max-width: 900px;
    font-size: 12px;
    > li {
      position: relative;
      margin-top: 8px;
      margin-left: 8px;
      hyphens: auto;
      @include high-media() {
        hyphens: none;
      }
      @extend %tg-ab-text;
      &::before {
        content: '';
        position: absolute;
        display: block;
        width: 4px;
        height: 4px;
        left: -8px;
        background-color: $primary-text-color;
        border-radius: 50%;
        margin-right: 4px;
        margin-top: 4px;
        flex: none;
      }
    }
  }
}

.a-table {
  border-spacing: 0;
  border-collapse: collapse;
  margin-top: 12px;

  &__cell {
    @include tg(12px, 500, 14px, 0.5px);
    padding: 12px;
    border: 1px solid rgb(209, 209, 209);
    max-width: 400px;
    vertical-align: top;
    &-8 {
      padding: 8px;
    }
    &-head {
      @include tg(16px, 600, 18px, 0.5px);
      text-align: left;
    }
    @include medium-media {
      text-overflow: ellipsis;
      overflow: hidden;
      padding: 4px;
      &-head {
        font-size: 14px;
      }
    }
  }
}

.ab {
  &__link {
    color: $primary-color;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    &:hover {
      color: #000;
    }
  }
}

.hiden {
  display: none;
}

.active {
  color: #000;
}
</style>
