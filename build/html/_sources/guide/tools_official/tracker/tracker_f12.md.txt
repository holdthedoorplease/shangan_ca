---
myst:
  html_meta:
    "description lang=zh": |
      Explore the various types of visitor visas to Canada and find the one that best suits your needs.
---

# ③ 查询是否被「安调」

<div class="dividing-line"></div>

```{gallery-grid}
:grid-columns: 1 2 2 3

- header: "{fas}`plane;pst-color-primary` ① 注册Tracker账号"
  content: "根据主申请人的UCI号码、签证申请号码等信息即可注册Tracker账号.通过中介申请也可注册。点击查看"
  link: "tracker_register.html"

- header: "{fas}`book;pst-color-primary` ② 查询「签证进度」"
  content: "使用Tracker账号即可查询签证处理进度：指纹、体检、申请资格、背景调查等环节的进展。点击查看"
  link: "tracker_check.html"

- header: "{fas}`users;pst-color-primary` ③ 查询是否被「安调」"
  content: "登陆Tracker后，可通过按「F12」或右键后选「检查」，查询是否被「安调」。点击查看"
  link: "tracker_f12.html"
```

<div class="dividing-line"></div>


## 手把手教程

1. 打开Tracker[官网](https://ircc-tracker-suivi.apps.cic.gc.ca/en/login)，输入Tracker账号和密码，点击`Sign in`

![Tracker查看安调状态 Step 1](/_static/images/guide/tools_official/tracker/05.png)

2. 找到主申请人`Principal applicant`，点击`View application history`

![Tracker查看安调状态 Step 2](/_static/images/guide/tools_official/tracker/06.png)

3. 在页面空白处点击右键，选择「检查」（Inspect）。如果你电脑的操作系统是Windows，则可直接按`F12`键。

![Tracker查看安调状态 Step 3](/_static/images/guide/tools_official/tracker/10.png)

4. 在弹出的页面中，点击左侧的控制台`Console`标签

![Tracker查看安调状态 Step 4](/_static/images/guide/tools_official/tracker/10-2.png)

5. 点击`Object`前面的小三角▶，将其展开

![Tracker查看安调状态 Step 5](/_static/images/guide/tools_official/tracker/11.png)

6. 点击`Relations`前面的小三角▶，将其展开

![Tracker查看安调状态 Step 6](/_static/images/guide/tools_official/tracker/12.png)

7. `Relations`后的`Array`的括号里有个数字，指这份签证里申请者的人数。可逐一点开查看

![Tracker查看安调状态 Step 7](/_static/images/guide/tools_official/tracker/13.png)

8. 点击数字前面的小三角▶，再点击`History`前面的小三角▶，展开详细内容

![Tracker查看安调状态 Step 8](/_static/images/guide/tools_official/tracker/14.png)

9. 在`History`的记录里，查看每一行最后的`Key`的值，看是否包含`Security`。如果包含，则看该行最前面的`actStatus`的值: 
- 如果`actStatus`的值为17, 则表示进入了「安调」
- 如果`actStatus`的值为33, 则表示已结束「安调」

![Tracker查看安调状态 Step 9](/_static/images/guide/tools_official/tracker/15.png)

<div class="dividing-line"></div>
