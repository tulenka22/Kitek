<template>
  <Navdrop :columns="columns" />
</template>

<script>
import { createLink, createColumn } from '~/core/helpers/link'
export default {
  name: 'NavdropStudent',
  data() {
    return {
      columns: [
        createColumn(
          '',
          createLink('/student/grafiks', 'График учебного процесса'),
          createLink('/student/schedule', 'Расписание занятий'),
          createLink('/student/contests', 'Конкурсы, олимпиады, конференции'),
          createLink('/student/mediacenter', 'Медиацентр «В ОБЪЕКТИВЕ КИТЭКА»')
        ),
        createColumn(
          '',
          createLink('/student/sportclub', 'Студенческий спортивный клуб «Старт»'),
          createLink('/student/assistance', 'Содействие трудоустройству выпускников'),
          createLink('/student/remote', 'Дистанционное обучение'),
          createLink('/student/sketchbook', '"Скетчбук СПО"')
        ),
        createColumn(
          '',
          createLink('/student/extramural', 'Заочное отделение'),
          createLink('/student/professionalitet', 'Теперь мы в "Профессионалитете"!'),
          createLink('/student/terror', 'Противодействие терроризму и экстремизму'),
          createLink('/student/railway', 'Железнодорожная безопасность'),
          createLink('/student/safety', 'Пожарная безопасность'),
          createLink('/student/livestudent', 'Студенческая жизнь: открывай мир, твори будущее!')
        ),
      ],
    }
  },
}
</script>
