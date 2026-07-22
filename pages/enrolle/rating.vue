<template>
  <block-ab title="Рейтинг абитуриентов">
    <common-input class="search" v-model.trim="search" placeholder="Фамилия Имя Отчество" />
    <!-- <p class="ab__p small__text">
      <a href="https://omsktec.ru/enrolle/orders" style="color: blue">Приказы о зачислении</a>
    </p> -->
    <p class="ab__p small__text">по состоянию на {{ data }}</p>

    <div v-if="readtable != ' '">
      <h2 class="ab__subtitle" v-for="spec in srecs" :key="spec.abgroup">
        <b red v-if="spec.abgroup == readtable">
          Специальность "{{ spec.name }}" ({{ spec.description }})
        </b>
        <b v-if="spec.abgroup == readtable">
          количество бюджетных мест {{ spec.p }}
        </b>
      </h2>
    </div>

    <p v-if="!documentsObj">{{ error }}</p>

    <ul v-else class="ab__list">
      <div class="ab__overflow">
        <table class="a-table">
          <thead v-if="readtable != ' '">
            <tr>
              <th class="a-table__cell a-table__cell-8 a-table__cell-center">№ п/п</th>
              <th class="a-table__cell a-table__cell-8 a-table__cell-center">
                Регистрационный <br />
                номер
              </th>
              <th class="a-table__cell a-table__cell-8 a-table__cell-center">Ф.И.О.</th>
              <th class="a-table__cell a-table__cell-8 a-table__cell-center">Средний балл</th>
              <th class="a-table__cell a-table__cell-8 a-table__cell-center">
                Документ об образовании
              </th>
            </tr>
          </thead>

          <tbody v-for="emp in documentsObj.table" :key="emp.delpole" v-show="table">
            <tr v-if="emp.abgroup == readtable" class="table__str-color">
              <!-- № п/п -->
              <td
                v-if="emp.fio == search"
                class="a-table__cell a-table__cell-8 a-table__cell-center result"
              >
                <b red>{{ emp.n }}</b>
              </td>
              <td
                v-else
                class="a-table__cell a-table__cell-8 a-table__cell-center"
              >
                <p>{{ emp.n }}</p>
              </td>

              <!-- Регистрационный номер -->
              <td
                v-if="emp.fio == search"
                class="a-table__cell a-table__cell-8 a-table__cell-center result"
              >
                {{ emp.id }}
              </td>
              <td
                v-else
                class="a-table__cell a-table__cell-8 a-table__cell-center"
              >
                {{ emp.id }}
              </td>

              <!-- ФИО -->
              <td
                v-if="emp.fio == search"
                class="a-table__cell a-table__cell-8 result"
              >
                <b red>{{ emp.fio }}</b>
              </td>
              <td
                v-else
                class="a-table__cell a-table__cell-8"
              >
                <p>{{ emp.fio }}</p>
              </td>

              <!-- Средний балл -->
              <td
                v-if="emp.fio == search"
                class="a-table__cell a-table__cell-8 a-table__cell-center result"
              >
                <b red>{{ emp.sba }}</b>
              </td>
              <td
                v-else
                class="a-table__cell a-table__cell-8 a-table__cell-center"
              >
                <p>{{ emp.sba }}</p>
              </td>

              <!-- Документ об образовании -->
              <td class="a-table__cell a-table__cell-8 a-table__cell-center">
                <p>{{ emp.doc }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </ul>

    <p v-if="!documentsObj">{{ error }}</p>

    <!-- Логика определения readtable по введённому ФИО -->
    <div v-else>
      <div v-for="(us, usIdx) of filteredTable" :key="usIdx">
        <p class="hiden" v-if="us.fio === search">
          {{ (readtable = us.abgroup) }}
        </p>
        <p class="hiden" v-if="us.fio != search">
          {{ (readtable = ' ') }}
        </p>
      </div>
    </div>

    <div class="contacts__row">
      <div class="contacts__row contacts__socials">
        <a href="https://vk.com/omsktec" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconVK />
          </IconWrapper>
        </a>
        <a href="https://ok.ru/group/53402328629468" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconOK />
          </IconWrapper>
        </a>
        <!-- <a href="https://t.me/omskkitec" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconTelegram />
          </IconWrapper>
        </a> -->
      </div>
    </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'

export default {
  data() {
    return {
      randomNum: Math.floor(Math.random() * 1000) + 1,
      table: true,
      employeers: [],
      // актуализированный список специальностей под abgroup из JSON
      srecs: [
        {
          abgroup: 'rmp',
          name: 'Разработка и управление программным обеспечением (Разработка мобильных приложений)',
          description: 'база: 9 класс, квалификация: программист',
          p: '25',
        },
        {
          abgroup: 'vr',
          name: 'Разработка и управление программным обеспечением (Веб-разработка)',
          description: 'база: 9 класс, квалификация: программист',
          p: '50',
        },
        {
          abgroup: 'tdk9',
          name: 'Торговое дело (Коммерция)',
          description: 'база: 9 класс, квалификация: специалист по торговому делу',
          p: '50',
        },
        {
          abgroup: 'tdk11',
          name: 'Торговое дело (Коммерция)',
          description: 'база: 11 класс, квалификация: специалист по торговому делу',
          p: '25',
        },
        {
          abgroup: 'tdt9',
          name: 'Торговое дело (Товароведение)',
          description: 'база: 9 класс, квалификация: специалист по торговому делу',
          p: '50',
        },
        {
          abgroup: 'tdt11',
          name: 'Торговое дело (Товароведение)',
          description: 'база: 11 класс, квалификация: специалист по торговому делу',
          p: '25',
        },
        {
          abgroup: 'b9',
          name: 'Экономика и бухгалтерский учет',
          description: 'база: 9 класс, квалификация: бухгалтер',
          p: '50',
        },
        {
          abgroup: 'b11',
          name: 'Экономика и бухгалтерский учет',
          description: 'база: 11 класс, квалификация: бухгалтер',
          p: '25',
        },
        {
          abgroup: 'tgg',
          name: 'Туризм и гостеприимство (Гостиничные услуги)',
          description: 'база: 9 класс, квалификация: специалист по туризму и гостеприимству',
          p: '25',
        },
        {
          abgroup: 'tge',
          name: 'Туризм и гостеприимство (Экскурсионные услуги)',
          description: 'база: 9 класс, квалификация: специалист по туризму и гостеприимству',
          p: '25',
        },
        {
          abgroup: 'tgp',
          name: 'Туризм и гостеприимство (Услуги предприятия питания)',
          description: 'база: 9 класс, квалификация: специалист по туризму и гостеприимству',
          p: '25',
        },
        {
          abgroup: 'pkd9',
          name: 'Поварское и кондитерское дело',
          description: 'база: 9 класс, квалификация: специалист по поварскому и кондитерскому делу',
          p: '100',
        },
        {
          abgroup: 'pkd11',
          name: 'Поварское и кондитерское дело',
          description: 'база: 11 класс, квалификация: специалист по поварскому и кондитерскому делу',
          p: '25',
        },
        {
          abgroup: 'pk',
          name: 'Повар, кондитер',
          description: 'база: 9 класс, квалификация: повар, кондитер',
          p: '75',
        },
        {
          abgroup: 'esu',
          name: 'Эксплуатация судовых энергетических установок',
          description: 'база: 9 класс, квалификация: техник-судомеханик',
          p: '75',
        },
        {
          abgroup: 'ztdk11',
          name: 'Торговое дело (Коммерция)',
          description: 'база: 11 класс (заочное отделение), квалификация: специалист по торговому делу',
          p: '25',
        },

      ],
      search: '',
      jsonPath: 'dynamic/rating/abiturients.json?' + this.randomNum,
      documentsObj: null,
      readtable: [],
      dublicateFio: [],
      error: 'Загрузка...',
    }
  },
  async created() {
    try {
      this.documentsObj = JSON.parse(await loadDynamic(this.jsonPath))
      this.employeers = this.documentsObj.table
      this.data = this.documentsObj.title
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
  methods: {
    includesLowercase(value, startsValue) {
      return value?.toLowerCase()?.includes(startsValue?.toLowerCase())
    },
  },
  computed: {
    filteredTable() {
      if (!this.search) return this.employeers
      return this.employeers.filter(
        (t) =>
          this.includesLowercase(t.fio, this.search) ||
          this.includesLowercase(t.abgroup, this.search)
      )
    },
  },
}
</script>

<style scoped lang="scss">
.rating {
  &__button {
    cursor: pointer;
    color: $accent-color;
    &:hover {
      color: $primary-text-color;
    }
  }
}
.search {
  margin-top: 12px;
  max-width: 1200px;
}
.result {
  background-color: rgb(211, 211, 211);
}
.hiden {
  visibility: hidden;
}
.small {
  &__text {
    @extend %tg-event-card-subtitle;
    @include medium-media() {
      font-size: 14px;
    }
  }
}
.ab {
  &__overflow {
    max-width: 100vw;
    overflow: auto;
  }
}
.click {
  cursor: pointer;
}
.contacts {
  flex: none;
  &__row {
    display: flex;
  }
  &__social {
    &:nth-child(even) {
      margin: 0 12px;
    }
  }
  &__socials {
    flex-grow: 1;
  }
}
</style>
