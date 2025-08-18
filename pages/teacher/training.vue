<template>
  <block-ab title="Повышение квалификации">
    <SplitLinks :links="links" />
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'

export default {
  data() {
    return {
      links: [
        createLink('https://apkpro.ru/', 'Академия Минпросвещения РФ'),
        createLink(
          'https://apkpro.ru/programmy/',
          'Образовательный портал Академии Минпросвещения РФ'
        ),
        createLink(
          'https://irooo.ru/obrazovanie/42-dopolnitelnye-professionalnye-programmy-povysheniya-kvalifikatsii',
          'Институт развития образования Омской области'
        ),
        createLink(
          'https://edu.irooo.ru/',
          'Образовательный портал Института развития образования Омской области'
        ),
        createLink(
          'https://omgpu.ru/dopolnitelnoe-obrazovanie',
          'Омский государственный педагогический университет'
        ),
        createLink(
          'https://omsk.ranepa.ru/dopolnitelnoe-obrazovanie/programmy-povysheniya-kvalifikatsii-i-professionalnoy-perepodgotovki.php',
          'РАНХиГС'
        ),
        createLink(
          'https://www.xn--d1abkefqip0a2f.xn--p1ai/index.php/kartochka-programmy',
          'Единый урок: календарь, методики, материалы'
        ),
        createLink(
          'https://education.apkpro.ru/',
          'Цифровая экосистема дополнительного профессионального образования'
        ),
        createLink(
          'https://cnppm.irooo.ru/spisok-kursov-i-kogo-zhdem#anchor',
          'ЦНППМ ПРОГРАММЫ ПОВЫШЕНИЯ КВАЛИФИКАЦИИ'
        ),
      ],
    }
  },
}
</script>

<style scoped lang="scss"></style>
