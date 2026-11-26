# City Game Studio + CGS Mega DLC — Thai glossary (binding)

## Style

1. Register B (default: buttons, menus, labels, tooltips, tutorials, finance/system text): friendly casual gamer Thai, short and clear, scene loanwords (เซฟ, โหลด, อัปเกรด, ปลดล็อก, บูสต์, โบนัส, สกิล, เกจ). No slang here.
2. Register C (only review catchphrases, NEW_ACHIEVEMENT_*, LOADING_*, random events, jokey mails, Mega DLC reviews/events): punchy community slang everybody knows (ปัง, แป้ก, จัดเต็ม, สุดๆ, เห็นๆ, โดนใจ, เทพ, กาก, เกลือ, 555). Glossary terms stay the same in both registers; only the wording around them changes.
3. Player = "คุณ" (drop it when Thai would). No ครับ/ค่ะ/คะ. No "." at sentence end; sentences separated by one space. No space before ! or ?. Repetition mark attached (แฟนๆ, เห็นๆ, สุดๆ).
4. Numbers: Arabic digits only, never Thai digits. Keep "$" and "%" exactly where the source has them ("$%s" stays "$%s", "%d%%" stays "%d%%"). Literal big numbers get commas (1 000 000 -> 1,000,000). Literal k/m in achievement text becomes Thai (100k -> 1 แสน, 500k -> 5 แสน, 1m -> 1 ล้าน, 100m -> 100 ล้าน); the unit-suffix labels LABEL_UNIT_K/M/G/T/P/E/Z/Y stay as Latin letters. "m²" -> "ตร.ม.".
5. Years stay in CE digits (1983, never พ.ศ.). "the 90s" -> "ยุค 90", "late 70s" -> "ปลายยุค 70". Month abbreviations use Thai forms (ม.ค. ... ธ.ค.).
6. Classifiers: แฟนๆ/พนักงาน/ผู้เล่น = คน, games = เกม, copies sold = ชุด, consoles and servers = เครื่อง, studios and buildings = แห่ง.
7. Genres: abbreviations stay Latin (RPG, FPS, TPS, RTS, RTT, 4X, MMO-RPG); genres with an everyday Thai name use it (ผจญภัย, สยองขวัญ, แข่งรถ, วางแผน); other loan genres are transliterated in Thai script (ทาวเวอร์ดีเฟนส์, วิชวลโนเวล); the developer's parody "-like" genres stay Latin (Crook-like, HTA-like, MOBA-like, Mystery-like). In running text say "เกมแนว X".
8. Job titles: Thai where a normal Thai title exists (นักบัญชี, ผู้จัดการการตลาด), loanword where the scene uses one (โปรดิวเซอร์, เทสเตอร์, แอดมินเครือข่าย). The three production phases are always ออกแบบ / พัฒนา / ขัดเกลา and their output is always "แต้ม" (score shown to the player is "คะแนน").
9. "Publish/Release" is split by meaning: your own game or console going on sale = วางขาย; an update, DLC, patch or demo = ปล่อย; acting as (or signing with) a publisher = จัดจำหน่าย. Keys containing EDIT / EDITION / TRADE are the publisher meaning.
10. Mail style: "Dear X," -> "ถึงคุณ X", "Hello/Hi" -> "สวัสดี", sign-offs -> "ด้วยความนับถือ". Confirm dialogs: "You are about to ..." -> "คุณกำลังจะ...", "Do you want to continue?" -> "จะทำต่อไหม?", "Are you sure ...?" -> "แน่ใจนะว่า...?".
11. Engine-feature and store-feature names are noun phrases without "การ" where possible (รองรับเมาส์, เซฟบนคลาวด์). Tier words are fixed: Basic = พื้นฐาน, Simple = แบบง่าย, Advanced = ขั้นสูง, Realistic = สมจริง.
12. Line wrapping: any Thai text over about 30 characters gets a normal space at clause/phrase boundaries so that no unbroken run exceeds about 30 characters; never inside a word or a glossary term.
13. When the English label is itself a mistranslation of the French original (noted below as "FR ..."), the Thai follows the French meaning.

## Glossary

| English | Thai | Notes |
|---|---|---|
| Studio | สตูดิโอ | Fixed. Both the dev team unit and the building type LABEL_BUILDING_STUDIO |
| Studio (LABEL_BUILDING_BIGSTUDIO) | สตูดิโอใหญ่ | FR "Grand studio"; only this key |
| Company | บริษัท | The player's or a rival's whole business |
| Company name | ชื่อบริษัท | |
| Game / Video game | เกม | Never "เกมส์". "Video game" is also เกม |
| Game engine / Engine | เอนจิน | Fixed. Never "เอนจิ้น" or "เกมเอนจิน" |
| Feature / Functionality | ฟีเจอร์ | Engine, digital-store and game features; BUTTON_CANCEL_FEATURE |
| Feature list | รายการฟีเจอร์ | |
| Module | โมดูล | "game engine modules", "Ad module" |
| Technology | เทคโนโลยี | "New technology available" |
| Genre / Game genre / Game type | แนวเกม | Fixed. Also LABEL_GAME_GENRE "Type" and "types of games" |
| Type | ประเภท | Building, campaign, training, event, platform, market-research type (not game genre) |
| Theme | ธีม | Fixed. Game theme; also UI theme |
| Interface theme | ธีมอินเทอร์เฟซ | LABEL_THEME_INTERFACE |
| Dark theme | ธีมมืด | Also LABEL_DARK_MODE |
| Light theme | ธีมสว่าง | |
| Combo | คอมโบ | Theme/genre combo |
| Platform | แพลตฟอร์ม | Fixed. Anything a game is released on |
| Console | คอนโซล | Game console hardware |
| Console (in-game command console) | คอนโซลคำสั่ง | Only LOADING_SCREEN_TIP_21 "Press F1 to open the in-game console" |
| Custom platform / Custom console / Own console | คอนโซลของตัวเอง | The console the player designs; same concept in all three wordings |
| Handheld console | คอนโซลพกพา | |
| Generation | เจเนอเรชัน | Console generation |
| Next-gen | เน็กซ์เจน | |
| Game size | ขนาดเกม | |
| Size | ขนาด | LABEL_GAME_SIZE and other bare "Size" labels |
| Indie | อินดี้ | Game size and "indie game" |
| Normal | ปกติ | Game size, game speed |
| Big | ใหญ่ | Game size |
| AAA | AAA | Game size; unchanged |
| Target audience / Targeted audience | กลุ่มเป้าหมาย | |
| Young | เด็ก | Audience |
| Everybody / Everyone | ทุกวัย | Audience |
| Mature | ผู้ใหญ่ | Audience |
| Sequel | ภาคต่อ | |
| Original game | เกมต้นฉบับ | |
| Previous game | ภาคก่อน | BUTTON_VIEW_PREVIOUS |
| Remake | รีเมค | Fixed |
| Remaster | รีมาสเตอร์ | Fixed |
| Franchise | แฟรนไชส์ | |
| New IP | IP ใหม่ | |
| Franchise fatigue / Fatigue | ความอิ่มตัว | Same word on the label and in TOOLTIP_FRANCHISE_FATIGUE |
| Franchise Health | สุขภาพแฟรนไชส์ | |
| Port | พอร์ต | Fixed. Verb: พอร์ตเกม |
| Game port | เกมพอร์ต | Noun: a ported version |
| Online game | เกมออนไลน์ | |
| Online multiplayer | มัลติเพลเยอร์ออนไลน์ | |
| Free-to-play | เล่นฟรี | |
| Free / Free of charge | ฟรี | |
| Paid | เสียเงิน | Paid game, paid update |
| Update | อัปเดต | Noun and verb |
| Free update | อัปเดตฟรี | |
| Paid update | อัปเดตเสียเงิน | Same concept as DLC in this game; follow the source wording |
| DLC | DLC | Unchanged |
| Patch | แพตช์ | |
| Bundle | บันเดิล | "pack your game with our console" = ขายบันเดิลกับคอนโซล |
| Demo | เดโม | |
| Prototype | ตัวต้นแบบ | |
| Alpha | อัลฟา | |
| Beta / Betas | เบต้า | "Beta version" = เวอร์ชันเบต้า |
| Early Access | Early Access | Unchanged; "Early Access Hub" = ศูนย์รวม Early Access |
| Game of the Year | เกมแห่งปี | |
| GOTY | GOTY | Abbreviation unchanged |
| Game of the Year edition | ฉบับเกมแห่งปี | BUTTON_PUBLISH_GOTY = วางขายฉบับ GOTY |
| Award / Prize | รางวัล | |
| Trophy | ถ้วยรางวัล | |
| Nominated | เข้าชิง | |
| Winner | ผู้ชนะ | |
| Runners-up | รองชนะเลิศ | |
| Catalog / Game catalog / Library | คลังเกม | |
| Game history | ผลงานเกม | FR "Portfolio"; list of games made |
| Project | โปรเจกต์ | |
| Mini-game / Minigame | มินิเกม | |
| Achievement | ความสำเร็จ | Steam-style achievements; also the digital-store feature |
| Leaderboard | ตารางอันดับ | |
| Roadmap | โรดแมป | |
| Event | อีเวนต์ | |
| News | ข่าว | |
| Design | ออกแบบ | Production phase and skill |
| Development | พัฒนา | Production phase, skill and finance category |
| Polish / Polishing | ขัดเกลา | Production phase and skill |
| Stage / Step | ขั้นตอน | "development stages", LABEL_STEP |
| Gauge / Slider | เกจ | Both words are the same game-creation bars |
| Workload | ปริมาณงาน | |
| Workload distribution | การกระจายงาน | |
| Points | แต้ม | Work output; never "คะแนน" |
| Design points | แต้มออกแบบ | |
| Development points | แต้มพัฒนา | |
| Polish points / Polishing points | แต้มขัดเกลา | |
| Genre points | แต้มแนวเกม | LABEL_SKILL_POINT(S); spent to unlock genres |
| Required points | แต้มที่ต้องใช้ | |
| Experience | ประสบการณ์ | "experience points" = แต้มประสบการณ์ |
| Blue zone / Blue area | โซนสีฟ้า | On gauges |
| White area | โซนสีขาว | On the workload chart |
| Balanced | สมดุล | Team, studio |
| Unbalanced | ไม่สมดุล | |
| Tips / Hints | เคล็ดลับ | Knowledge from post-mortems and contracts; also loading tips |
| Gameplay | เกมเพลย์ | Gauge |
| Graphics | กราฟิก | Gauge; never "กราฟฟิก" |
| Sound | เสียง | Gauge |
| Music | ดนตรี | Gauge, engine feature, theme |
| SoundFX | ซาวด์เอฟเฟกต์ | |
| Story | เนื้อเรื่อง | Gauge |
| Cutscenes | คัตซีน | Gauge |
| Cinematics | ซีนีมาติก | Engine features only |
| Characters | ตัวละคร | |
| Dialog | บทสนทนา | |
| Artwork | อาร์ตเวิร์ก | |
| Animation | แอนิเมชัน | |
| Physics | ฟิสิกส์ | |
| Artificial Intelligence | ปัญญาประดิษฐ์ | When spelled out |
| AI | AI | Abbreviation unchanged |
| Scripting | สคริปต์ | |
| Network | เครือข่าย | Gauge |
| Modding | ระบบม็อด | Gauge and feature unlock |
| User interface | อินเทอร์เฟซ | Gauge; "UI" stays UI |
| Tutorial | บทช่วยสอน | Gauge, engine feature, and the game's own tutorials |
| Optimization | ออปติไมซ์ | |
| Marketing material | สื่อการตลาด | |
| Customization | ปรับแต่ง | |
| Navigation | การนำทาง | |
| Miscellaneous / Misc | อื่นๆ | |
| Kick off | คิกออฟ | |
| Legacy code | โค้ดเก่า | |
| Rewrite | เขียนใหม่ | Engine |
| Proprietary | แบบขายไลเซนส์ | Engine licence model |
| FOSS | FOSS | Unchanged |
| Free and Open Source Software | ซอฟต์แวร์เสรีและโอเพนซอร์ส | |
| In-house / Internal | ใช้ภายใน | LABEL_OWNER, LABEL_PREFER_HOME_MADE |
| Made with | สร้างด้วย | LABEL_TOOLS |
| Employee / Staff | พนักงาน | Both words, everywhere |
| Team | ทีม | |
| Headcount | จำนวนพนักงาน | |
| Developer | นักพัฒนา | A staff member (LABEL_STAFF_DEV_SIZE, "Requires %d developer") |
| Developer (LABEL_DEVELOPER, LABEL_DEVELOPPER_NAME) | ผู้พัฒนา | The company credited on a game |
| Designer | นักออกแบบ | |
| Tester | เทสเตอร์ | |
| Specialist | ผู้เชี่ยวชาญ | Producer, accountant, HR, marketing manager, network admin |
| Producer | โปรดิวเซอร์ | Staff specialist; also difficulty 4 name |
| Studio director | ผู้อำนวยการสตูดิโอ | |
| Director | ผู้อำนวยการ | Short form of studio director in tooltips |
| Accountant | นักบัญชี | |
| Human resources / Human resources manager | ฝ่ายบุคคล | Staff role and finance category |
| HR | HR | Abbreviation unchanged |
| Marketing manager | ผู้จัดการการตลาด | |
| Network administrator | แอดมินเครือข่าย | |
| Community manager | คอมมูนิตี้เมเนเจอร์ | |
| Sound composer | นักแต่งเพลง | |
| UI Designer | นักออกแบบ UI | |
| QA tester | เทสเตอร์ QA | Difficulty 1 name |
| Game developer | นักพัฒนาเกม | Difficulty 2 name |
| Engine developer | นักพัฒนาเอนจิน | Difficulty 3 name |
| CEO | CEO | Difficulty 5 name; unchanged |
| Founder | ผู้ก่อตั้ง | |
| Boss | บอส | How staff address the player |
| Candidate | ผู้สมัคร | |
| Skills / Capability | สกิล | Employee skills; "areas of competence" too |
| Level | เลเวล | Skill level |
| Productivity / Prod. | ประสิทธิภาพ | No Thai abbreviation; write it in full |
| Performance | ความลื่นของเกม | Graphics-option tooltips only ("impact on performance") |
| Happiness | ความสุข | |
| Energy | พลังงาน | |
| Salary | เงินเดือน | |
| Pay raise / Wage increase | ขึ้นเงินเดือน | |
| Payroll | เงินเดือนพนักงาน | |
| Hiring costs | ค่าจ้างพนักงานใหม่ | |
| Date of hire | วันที่จ้าง | |
| Holiday / Vacation | พักร้อน | "Send on vacation" = ส่งไปพักร้อน |
| Training | ฝึกอบรม | |
| General training | ฝึกอบรมทั่วไป | |
| Specific training | ฝึกอบรมเฉพาะด้าน | |
| Auto-training | ฝึกอบรมอัตโนมัติ | |
| University | มหาวิทยาลัย | |
| Lecture hall | ห้องบรรยาย | |
| Classroom | ห้องเรียน | |
| Seats | ที่นั่ง | |
| Hire / Recruit | จ้าง | Fixed |
| Fire | ไล่ออก | Fixed |
| Poach | ดึงตัว | BUTTON_HIRE_THEIR_EMPLOYE |
| Lay off | ปลดพนักงาน | |
| Resignation | ลาออก | |
| Job application | ใบสมัครงาน | |
| Assign | มอบหมาย | |
| Unassign / Withdraw / Remove | ถอน | Taking staff or specialists off a task |
| Transfer | ย้าย | Employees between studios |
| Auto-assign / Automatic assignment | มอบหมายอัตโนมัติ | |
| Assignments | การมอบหมาย | BUTTON_RESET_SCHEDULE |
| Planning / Schedule | ตารางงาน | LABEL_PLANNING is FR "planning" = staff schedule |
| Idle | ว่าง | Staff, studio |
| Busy | ไม่ว่าง | |
| Work | ทำงาน | LABEL_WORKING (verb) |
| Status | สถานะ | LABEL_WORK |
| Perfect | เพอร์เฟกต์ | Maxed-out employee; "Perfect game" |
| Bored | เบื่อ | Staff tired of a genre |
| Publisher | ผู้จัดจำหน่าย | Fixed |
| Publish (as or with a publisher) | จัดจำหน่าย | Keys with EDIT / EDITION / TRADE; "Number of published games" |
| Publish / Release (own game or console) | วางขาย | LABEL_RELEASE, "Games released", "Release everything" |
| Publish / Release (update, DLC, patch, demo) | ปล่อย | "Publish an update" = ปล่อยอัปเดต |
| Publication date | วันที่เผยแพร่ | Mods only |
| Release date | วันวางขาย | |
| Announce | ประกาศเปิดตัว | Game or console announcement; plain press statements may use ประกาศ |
| Self-publishing | จัดจำหน่ายเอง | |
| Traditional publishing | ผ่านผู้จัดจำหน่าย | LABEL_TRADE_PUBLISH |
| Publishing offer | ข้อเสนอจัดจำหน่าย | |
| Publishing contract | สัญญาจัดจำหน่าย | |
| Contract | งานรับจ้าง | Contract work as a project type: LABEL_CONTRACT, BUTTON_CANCEL_CONTRACT, "No contract available", TOOLTIP_MENU_CREATE_GAME, TOOLTIP_TIPS_CAPACITY |
| Contract (agreement) | สัญญา | Publishing, exclusivity, loan paperwork; LABEL_FILTER_ONLY_CONTRACTS |
| Exclusivity deal / Exclusive contract / Exclusive offer | สัญญาเอ็กซ์คลูซีฟ | |
| Exclusive / Exclusivity | เอ็กซ์คลูซีฟ | "Exclusivity duration" = ระยะเวลาเอ็กซ์คลูซีฟ |
| Devkit / Development kit | เดฟคิต | |
| License | ไลเซนส์ | Engine and platform licences |
| Royalties / Royalty | ค่าลิขสิทธิ์ | |
| Royalty free | ไม่คิดค่าลิขสิทธิ์ | |
| All rights reserved | สงวนลิขสิทธิ์ | |
| Offer | ข้อเสนอ | |
| Deal | ดีล | |
| Negotiate | เจรจา | |
| Counteroffer | ข้อเสนอสวนกลับ | |
| Trading panel | หน้าเจรจา | FR "Panneau des négociations" |
| Relationship | ความสัมพันธ์ | With manufacturers |
| Friendly | เป็นมิตร | |
| Neutral | เป็นกลาง | |
| Unfriendly | ไม่เป็นมิตร | |
| Partnership | ความร่วมมือ | |
| Competitor / Competition / Rival | คู่แข่ง | Fixed. "rival studio" = สตูดิโอคู่แข่ง |
| Acquire / Acquisition / Buy out | ซื้อกิจการ | Of a competitor. "Acquire all games/studios/staff" = รับ...ทั้งหมด |
| Spy (verb) | สอดแนม | "Spy on a competitor" = สอดแนมคู่แข่ง |
| Force a studio sale | บีบให้ขายสตูดิโอ | |
| Break the law | ทำผิดกฎหมาย | |
| Manufacturer | ผู้ผลิต | Console maker |
| Component / Part | ชิ้นส่วน | Console parts |
| Console case | เคสคอนโซล | |
| Cartridge | ตลับเกม | |
| Controller | คอนโทรลเลอร์ | |
| Processor | CPU | LABEL_PLATFORM_COMPONENT_CPU |
| Graphics card | การ์ดจอ | |
| Hard drive | ฮาร์ดดิสก์ | |
| Memory | หน่วยความจำ | |
| Screen | หน้าจอ | |
| Compute capabilities / Computing power | พลังประมวลผล | |
| Graphics capabilities | พลังกราฟิก | |
| Capabilities | ขีดความสามารถ | "the console's capabilities" |
| Quality | คุณภาพ | |
| Manufacturing costs | ต้นทุนการผลิต | |
| Units sold | จำนวนที่ขายได้ | |
| Copies | ชุด | Game copies: "1 ล้านชุด" |
| Unit | เครื่อง | A console unit: "Profit per unit" = กำไรต่อเครื่อง |
| Units returned | เครื่องที่ถูกคืน | |
| Refund | คืนเงิน | |
| Discontinue / Halt production | เลิกผลิต | A console. For the digital store "stop supporting platform" = เลิกรองรับ |
| End of life | ใกล้เลิกผลิต | |
| Backwards compatibility | รองรับเกมรุ่นก่อน | |
| Compatibility | ความเข้ากันได้ | Between platforms for ports |
| Copy protection | ระบบกันก๊อปปี้ | |
| DRM | DRM | Unchanged |
| Piracy | การละเมิดลิขสิทธิ์ | |
| Crack | แคร็ก | Fixed. "Crack this game" = แคร็กเกมนี้ |
| Cracked | โดนแคร็ก | Status |
| Cracker | แคร็กเกอร์ | |
| Hack | แฮ็ก | Verb, theme |
| Hacker | แฮกเกอร์ | |
| Firewall | ไฟร์วอลล์ | |
| Virus | ไวรัส | |
| Anti-cheat | ระบบกันโกง | |
| Bot protection | ระบบกันบอต | |
| Fans | แฟนๆ | Fixed |
| Fan base / Fanbase | ฐานแฟน | |
| Hype | กระแส | Fixed. "Hype bonus" = โบนัสกระแส |
| Review | รีวิว | Noun and verb; also the digital-store feature |
| Review score | คะแนนรีวิว | Fixed |
| Score / Grade / Rating | คะแนน | "Average score" = คะแนนเฉลี่ย; "Score min." = คะแนนขั้นต่ำ |
| Overall Reviews | รีวิวโดยรวม | |
| Overwhelmingly positive | แง่บวกอย่างท่วมท้น | Steam's Thai wording |
| Very positive | แง่บวกเป็นอย่างมาก | |
| Mostly positive | แง่บวกเป็นส่วนใหญ่ | |
| Mixed | ผสมกัน | |
| Mostly negative | แง่ลบเป็นส่วนใหญ่ | |
| Very negative | แง่ลบเป็นอย่างมาก | |
| Overwhelmingly negative | แง่ลบอย่างท่วมท้น | |
| Critics | นักวิจารณ์ | |
| Press (noun) | สื่อ | Game media: "Talk to the press", "press ratings" |
| Magazine | นิตยสาร | |
| Popularity | ความนิยม | |
| Visibility | การมองเห็น | Of games; also mod visibility |
| Trend | เทรนด์ | "Fan base trends", "Theme trends" |
| Trending / Trendy | มาแรง | |
| Market | ตลาด | |
| Market share | ส่วนแบ่งตลาด | |
| Market research | วิจัยตลาด | |
| Analyze / Study | วิเคราะห์ | Market research actions |
| Interest | ความสนใจ | "Interest in the selected game genre" |
| Match | ความเข้ากัน | Genre/theme/platform/audience match |
| Excellent match | เข้ากันยอดเยี่ยม | |
| Good match | เข้ากันดี | |
| OK match | เข้ากันพอใช้ | |
| Poor match | เข้ากันแย่ | |
| Excellent | ยอดเยี่ยม | Rating adjective |
| Good | ดี | Rating adjective |
| OK | พอใช้ | Rating adjective; the button "Ok" is ตกลง |
| Poor | แย่ | Rating adjective |
| essential | ขาดไม่ได้ | Post-mortem importance scale |
| very important | สำคัญมาก | Post-mortem importance scale |
| relatively important | ค่อนข้างสำคัญ | Post-mortem importance scale |
| marginal | สำคัญเล็กน้อย | Post-mortem importance scale |
| insignificant | แทบไม่สำคัญ | Post-mortem importance scale |
| Post-mortem / Postmortem / Game report | สรุปบทเรียนหลังวางขาย | Fixed. All three English wordings |
| Players | ผู้เล่น | People who play the player's games |
| Player name | ชื่อผู้เล่น | The person playing City Game Studio |
| Users | ผู้ใช้ | Digital-store accounts |
| Concurrent users | ผู้ใช้พร้อมกัน | |
| Customers | ลูกค้า | |
| Community | คอมมูนิตี้ | |
| Wishlist | วิชลิสต์ | Noun and verb |
| Marketing | การตลาด | |
| Marketing campaign | แคมเปญการตลาด | |
| Advertising campaign | แคมเปญโฆษณา | |
| Campaign type | ประเภทแคมเปญ | |
| Ads / Advertising | โฆษณา | |
| Ad banner | แบนเนอร์โฆษณา | |
| Ad popup | โฆษณาป๊อปอัป | |
| Popup | ป๊อปอัป | |
| Talk to the press | คุยกับสื่อ | |
| Publish a demo | ปล่อยเดโม | |
| Television / TV | ทีวี | Marketing channel and furniture |
| Newsletter | จดหมายข่าว | |
| Email / Mail | อีเมล | |
| Website | เว็บไซต์ | |
| Online advertising | โฆษณาออนไลน์ | |
| Social networks | โซเชียลมีเดีย | |
| Advertising billboard | ป้ายบิลบอร์ด | |
| Targeted advertising campaign | แคมเปญโฆษณาเจาะกลุ่ม | |
| Spam | สแปม | |
| Inbox | กล่องข้อความ | |
| Message | ข้อความ | |
| Interview | สัมภาษณ์ | |
| Convention | งานเกม | Fixed |
| Exhibition center | ศูนย์แสดงสินค้า | LABEL_CONVENTION, LABEL_BUILDING_CONVENTION |
| Stand | บูธ | "Stand size" = ขนาดบูธ |
| Visitors | ผู้เข้าชม | |
| Attendance | จำนวนผู้เข้าชม | |
| Attend / Participate | เข้าร่วม | |
| Attending | เข้าร่วมแล้ว | LABEL_ALREADY_REGISTERED |
| Organize | จัดงาน | "Organize a convention" = จัดงานเกม |
| Festival | เทศกาล | Digital-store event |
| Tiny crowd | คนบางตา | |
| Small crowd | คนน้อย | |
| Regular Crowd | คนปานกลาง | |
| Big crowd | คนเยอะ | |
| Huge crowd | คนแน่นขนัด | |
| Low | ต่ำ | |
| Mid | กลาง | |
| High | สูง | |
| Money / Cash | เงิน | "Available cash" = เงินสดคงเหลือ |
| Currency | เงิน | In-game money (FR "Argent"); "Unlimited currency" = เงินไม่จำกัด |
| Income | รายรับ | |
| Revenue | รายได้ | |
| Estimated revenue | รายได้โดยประมาณ | LABEL_ESTIMATED_INCOME |
| Expenses | รายจ่าย | Also LABEL_OUTCOME |
| Profit / Profits | กำไร | |
| Net profit | กำไรสุทธิ | |
| Profitable | ทำกำไร | |
| Not profitable | ขาดทุน | |
| Costs | ค่าใช้จ่าย | Generic running costs |
| Development cost | ค่าพัฒนา | |
| Fixed costs | ต้นทุนคงที่ | |
| Cost of Goods Sold | ต้นทุนขาย | |
| Cost efficiency | ความคุ้มค่า | |
| Total | รวม | "Total costs" = ค่าใช้จ่ายรวม |
| Price | ราคา | |
| Selling price | ราคาขาย | |
| Buy price | ราคาซื้อ | |
| Suggested retail price | ราคาขายปลีกแนะนำ | |
| Discount | ส่วนลด | "Offer a discount" = จัดลดราคา |
| Sales | ยอดขาย | Units or money earned |
| Sales (LABEL_DS_SALES_TITLE, LABEL_DS_SALES_DESCRIPTION, Mega "Sales") | ลดราคา | FR "Soldes": discount events on the digital store |
| Sales boost / Sales bonus | โบนัสยอดขาย | |
| Rent (verb) | เช่า | BUTTON_RENT, BUTTON_BUILDING_RENT |
| Rent / Lease (noun) | ค่าเช่า | LABEL_RENT, LABEL_BUILDING_LEASE, annual report |
| Maintenance | ค่าบำรุงรักษา | |
| Taxes | ภาษี | |
| Tax reduction | ลดหย่อนภาษี | |
| Bank | ธนาคาร | |
| Banker | นายธนาคาร | |
| Loan | เงินกู้ | "Last-resort loan" = เงินกู้ทางเลือกสุดท้าย |
| Repay | ชำระคืน | |
| Interest rate | อัตราดอกเบี้ย | Loans; not the genre "Interest" |
| Mortgage | เงินกู้จำนอง | "take out a mortgage" = กู้จำนอง |
| Monthly payment | ค่างวดรายเดือน | |
| Debt | หนี้ | |
| Bankruptcy | ล้มละลาย | "Declare bankruptcy" = ประกาศล้มละลาย |
| Donation | เงินบริจาค | |
| Grant | เงินสนับสนุน | |
| Penalty | ค่าปรับ | Money owed under a contract or court ruling |
| Penalty (engine legacy code) | เพนัลตี้ | Extra points/cost when updating an old engine |
| Bonus | โบนัส | |
| Boost | บูสต์ | |
| Dividends | เงินปันผล | |
| Share / Stock | หุ้น | Company shares |
| Stock market | ตลาดหุ้น | |
| Shareholder | ผู้ถือหุ้น | |
| Profit Share / Cut | ส่วนแบ่งกำไร | Studio director's cut; "Digital store cut" = ส่วนแบ่งของร้านค้าดิจิทัล |
| Order | คำสั่งซื้อขาย | Stock orders; "Order sent" = ส่งคำสั่งแล้ว |
| Investor | นักลงทุน | |
| Value | มูลค่า | "Furniture value", "Value of shares" |
| Property value | มูลค่าทรัพย์สิน | |
| Real estate | อสังหาริมทรัพย์ | |
| Land value | มูลค่าที่ดิน | |
| Financial details | รายละเอียดการเงิน | |
| Annual Report | รายงานประจำปี | |
| Fiscal Year | ปีงบประมาณ | |
| Subscription | ค่าสมาชิก | Monthly fee of an online game; "Subscription price" = ราคาค่าสมาชิก |
| Subscribe (mods) | ติดตาม | Steam Workshop; "Unsubscribe" = เลิกติดตาม |
| Microtransactions | ไมโครทรานแซกชัน | |
| Lootbox | กล่องสุ่ม | |
| Cosmetic | ไอเทมตกแต่ง | |
| Power boost | บูสต์พลัง | |
| Power factor | ระดับพลัง | |
| Pack | แพ็ก | "Pack #%d" = แพ็ก #%d |
| Item | ไอเทม | Microtransaction and inventory items |
| Item (build mode) | ของ | Furniture being placed: "to rotate the item" = หมุนของ |
| Rarity | ความหายาก | |
| Uncommon | ไม่ธรรมดา | |
| Rare | หายาก | |
| Epic | เอพิก | |
| Legendary | ระดับตำนาน | |
| Digital store | ร้านค้าดิจิทัล | Fixed |
| Store | ร้านค้า | Digital-store feature LABEL_DS_STORE_TITLE |
| Shop | ร้านเฟอร์นิเจอร์ | LABEL_SHOP_UI: furniture shop inside a studio |
| Analytics | ระบบวิเคราะห์ข้อมูล | Digital-store feature |
| Chat | แชต | Digital-store feature; Twitch chat |
| Cross-platform | ข้ามแพลตฟอร์ม | Digital-store feature and engine feature |
| Forum | ฟอรัม | |
| Gift cards | บัตรของขวัญ | |
| Inventory | คลังไอเทม | |
| Marketplace | ตลาดซื้อขาย | |
| Support | ซัพพอร์ต | Digital-store feature (technical support) |
| Support (verb) | รองรับ | "Support all platforms", "Mouse support" = รองรับเมาส์ |
| Workshop | เวิร์กช็อป | "Steam workshop" stays Steam Workshop |
| Game Pass | Game Pass | Mega DLC store feature; unchanged |
| Free Play Days | วันเล่นฟรี | Mega DLC |
| Coins | เหรียญ | Mega DLC |
| Offline Store | ร้านค้าออฟไลน์ | Mega DLC |
| Christmas Sale | ลดราคาคริสต์มาส | Mega DLC |
| Seasonal Sale | ลดราคาตามฤดูกาล | Mega DLC |
| Themes & Skins | ธีมและสกิน | Mega DLC |
| Voice-Chat Overlay | โอเวอร์เลย์แชตเสียง | Mega DLC |
| Streaming-Hub | ศูนย์รวมสตรีม | Mega DLC |
| Screenshots | สกรีนช็อต | Mega DLC |
| Secure Payment Protection | ระบบชำระเงินปลอดภัย | Mega DLC |
| Price Tracker | ตัวติดตามราคา | Mega DLC |
| Server | เซิร์ฟเวอร์ | |
| Server load | ภาระเซิร์ฟเวอร์ | Not "โหลด", which is kept for loading saves |
| Server capacity | ความจุเซิร์ฟเวอร์ | |
| Total player capacity | ความจุผู้เล่นทั้งหมด | |
| Rented servers | เซิร์ฟเวอร์เช่า | |
| Owned servers | เซิร์ฟเวอร์ของตัวเอง | |
| Owned | เป็นเจ้าของ | Status of buildings |
| Dedicated server | เซิร์ฟเวอร์ Dedicated | |
| Low latency server | เซิร์ฟเวอร์ความหน่วงต่ำ | |
| Cloud | คลาวด์ | |
| Cloud computing | คลาวด์คอมพิวติง | |
| Online player count | จำนวนผู้เล่นออนไลน์ | |
| Threshold | เกณฑ์ | |
| Building | อาคาร | |
| Office | ออฟฟิศ | |
| Apartment | อพาร์ตเมนต์ | |
| Residence | ที่พักอาศัย | |
| Café | คาเฟ่ | |
| Gym | ยิม | |
| Hotel | โรงแรม | |
| Pizzeria | ร้านพิซซ่า | |
| Restaurant | ร้านอาหาร | |
| Theater | โรงละคร | |
| Tower | ตึกสูง | |
| Road / Street | ถนน | |
| Square | จัตุรัส | |
| Grass | ที่ดิน | Empty building plot (FR "Terrain") |
| Area / Surface / Square footage | พื้นที่ | |
| City map | แผนที่เมือง | |
| Map size | ขนาดแผนที่ | |
| Build | สร้าง | |
| Build mode | โหมดสร้าง | |
| Edit studio | แก้ไขสตูดิโอ | |
| Demolish / Destroy | รื้อถอน | Buildings |
| Renovate | รีโนเวต | |
| Layout | ผังห้อง | "Copy studio layout" = คัดลอกผังห้องสตูดิโอ |
| Auto-furnish | จัดเฟอร์นิเจอร์อัตโนมัติ | |
| Furniture | เฟอร์นิเจอร์ | |
| Desk | โต๊ะทำงาน | |
| Table | โต๊ะ | |
| Computer | คอมพิวเตอร์ | |
| Coffee machine | เครื่องชงกาแฟ | |
| Vending machine | ตู้กดน้ำ | |
| Water fountain | ตู้น้ำดื่ม | |
| Plant | ต้นไม้ | |
| Sofa / Couch | โซฟา | |
| Armchair | เก้าอี้นวม | |
| Bookshelf | ชั้นหนังสือ | |
| Whiteboard | ไวต์บอร์ด | |
| Printer | เครื่องพิมพ์ | |
| Wastebasket / Trash | ถังขยะ | |
| Foosball | โต๊ะฟุตบอล | |
| Air Hockey | แอร์ฮอกกี้ | |
| Pinball | พินบอล | "Pinball Sneak In" = พินบอล Sneak In |
| Arcade | ตู้อาร์เคด | "Arcade City Game Studio" = ตู้อาร์เคด City Game Studio |
| Door | ประตู | |
| Wall | ผนัง | |
| Floor | พื้น | |
| Pillar | เสา | |
| Metal | โลหะ | Furniture material: "Metal desk" = โต๊ะทำงานโลหะ |
| Wood | ไม้ | Furniture material |
| Stray cat | แมวจร | |
| Adopt | รับเลี้ยง | |
| Abandon | ทิ้ง | Cat event; "Abandon the building" = ทิ้งอาคาร |
| Save / Savegame | เซฟ | Noun |
| Save game | เซฟเกม | Verb/button |
| Load | โหลด | Saves and loading screens |
| Autosave / Automatic saving | เซฟอัตโนมัติ | |
| Overwrite | เซฟทับ | |
| Corrupted save | เซฟเสีย | |
| Mod | ม็อด | |
| Mod support | รองรับม็อด | |
| Sandbox mode | โหมดแซนด์บ็อกซ์ | |
| Historical Mode | โหมดอิงประวัติศาสตร์ | |
| Advanced start | เริ่มแบบขั้นสูง | |
| Difficulty | ระดับความยาก | Game setting and engine feature |
| Easy | ง่าย | |
| Challenging / Hard | ยาก | LABEL_HARD |
| Insane | โหดสุด | |
| Realistic | สมจริง | Mega DLC difficulty; also the engine-feature tier |
| easiest | ง่ายสุด | |
| hardest | ยากสุด | |
| Game speed | ความเร็วเกม | |
| Slowest | ช้าสุด | |
| Slow | ช้า | |
| Fast | เร็ว | Mega DLC |
| Fastest | เร็วสุด | Mega DLC |
| Tiny | จิ๋ว | Map size |
| Small | เล็ก | Map size; "small game" = เกมเล็ก |
| Medium | กลาง | Map size |
| Large | ใหญ่ | Map size; "large game" = เกมใหญ่ |
| Huge | ใหญ่มาก | Map size |
| EXTREME | สุดขีด | Mega DLC map size |
| Ultimate Size | ขนาดอัลติเมต | Mega DLC map size |
| New game | เริ่มเกมใหม่ | BUTTON_NEW_GAME: start a new playthrough |
| New game (create a game project) | สร้างเกมใหม่ | NEW_GAME, TOOLTIP_CREATE_GAME. LABEL_NEW_GAME and BUTTON_NEW_GAME start a new save = เริ่มเกมใหม่ |
| Load game | โหลดเกม | |
| Main menu | เมนูหลัก | |
| Options | ตัวเลือก | |
| Settings | ตั้งค่า | "Graphics settings" = ตั้งค่ากราฟิก |
| Help | ช่วยเหลือ | |
| Credits | เครดิต | |
| Special thanks | ขอบคุณเป็นพิเศษ | |
| Quit / Exit | ออกจากเกม | |
| Game over | เกมโอเวอร์ | Also LABEL_LOSE |
| Language | ภาษา | |
| Fullscreen | เต็มจอ | |
| Windowed | หน้าต่าง | |
| Borderless | ไร้ขอบ | |
| Resolution | ความละเอียด | |
| Larger font | ตัวอักษรใหญ่ขึ้น | |
| Grid | กริด | |
| Pause | หยุดชั่วคราว | "Auto pause" = หยุดเกมอัตโนมัติ |
| Version | เวอร์ชัน | |
| Restart required | ต้องรีสตาร์ต | |
| Accept | ยอมรับ | |
| Refuse / Decline | ปฏิเสธ | |
| Apply | ใช้ | |
| Previous | ก่อนหน้า | BUTTON_BACK (FR "Précédent") |
| Back | กลับ | Returning to a screen ("Back to Desktop" = กลับสู่เดสก์ท็อป); LABEL_TRANS_BACK is an easing name and stays "Back" |
| Next | ถัดไป | |
| Skip | ข้าม | |
| Start | เริ่ม | |
| Continue | ไปต่อ | |
| Cancel | ยกเลิก | |
| Cancel all | ยกเลิกทั้งหมด | |
| Confirm | ยืนยัน | |
| Ok | ตกลง | Button |
| Yes | ใช่ | |
| No | ไม่ | |
| Close | ปิด | |
| Buy | ซื้อ | |
| Sell | ขาย | |
| Pay | จ่าย | |
| Create / Make | สร้าง | A game, engine, console, mod |
| Develop | พัฒนา | "in development" = กำลังพัฒนา |
| Edit | แก้ไข | |
| Delete | ลบ | |
| Delete all | ลบทั้งหมด | |
| Rename | เปลี่ยนชื่อ | |
| Copy | คัดลอก | |
| Reset | รีเซ็ต | |
| Restore | กู้คืน | |
| Select | เลือก | |
| Select all | เลือกทั้งหมด | |
| Select none | ไม่เลือกเลย | |
| Search | ค้นหา | |
| Filter by | กรองตาม | |
| Sort by | เรียงตาม | |
| View | ดู | "View game" = ดูเกม |
| Show | แสดง | |
| Hide | ซ่อน | |
| Details | รายละเอียด | Also LABEL_INFORMATIONS |
| Overview | ภาพรวม | |
| Charts | กราฟ | |
| List | รายการ | "Studio list" = รายการสตูดิโอ |
| Read | อ่าน | |
| Clear | ล้าง | |
| Import | นำเข้า | |
| Validate | ตรวจสอบ | Mods |
| Upgrade | อัปเกรด | |
| Unlock | ปลดล็อก | |
| Unlocked | ปลดล็อกแล้ว | |
| Locked | ล็อกอยู่ | |
| Give up | ยอมแพ้ | |
| Keep playing | เล่นต่อ | |
| Too bad | เสียดายจัง | |
| Let's go! | ลุยเลย! | |
| Press (verb) | กด | "Press this button", "Press any key"; never "คลิก" |
| Bug report | แจ้งบั๊ก | |
| Feedback | ส่งความเห็น | |
| Zoom | ซูม | |
| Mark as spam | ทำเป็นสแปม | |
| Enabled | เปิด | |
| Disabled | ปิดอยู่ | |
| Available | พร้อมใช้ | Features, platforms, contracts |
| Available (studio, employee, desk) | ว่าง | "No studio available" = ไม่มีสตูดิโอว่าง |
| Not available | ไม่พร้อมใช้ | |
| Complete | เสร็จแล้ว | |
| Success | สำเร็จ | |
| Failure | ล้มเหลว | |
| Expired | หมดอายุ | |
| Canceled | ยกเลิกแล้ว | |
| Released | วางขายแล้ว | |
| Discontinued | เลิกผลิตแล้ว | |
| Required / Needed | ต้องใช้ | |
| Unique | ไม่ซ้ำใคร | A genre nobody else has unlocked yet |
| Default | ค่าเริ่มต้น | |
| None | ไม่มี | |
| maximum | สูงสุด | |
| minimum | ต่ำสุด | |
| currently | ตอนนี้ | |
| or | หรือ | |
| (if possible) | (ถ้าทำได้) | |
| Loading | กำลังโหลด | |
| Downloading | กำลังดาวน์โหลด | |
| Connection lost | ขาดการเชื่อมต่อ | |
| Private | ส่วนตัว | Mod visibility |
| Public | สาธารณะ | Mod visibility |
| Friends only | เฉพาะเพื่อน | Mod visibility |
| Not listed | ไม่แสดงในรายการ | Mod visibility |
| Poll | โพล | Twitch |
| Token | โทเคน | Twitch |
| Week / weeks | สัปดาห์ | |
| Month | เดือน | |
| Year / Years | ปี | |
| Monthly | รายเดือน | |
| Yearly / Annual | รายปี | |
| minutes | นาที | |
| seconds | วินาที | |
| Last 12 months | 12 เดือนล่าสุด | |
| Duration | ระยะเวลา | |
| Due date | วันครบกำหนด | LABEL_DATE |
| Creation date | วันที่สร้าง | |
| Starting year | ปีเริ่มต้น | |
| quarter | ไตรมาส | |
| JAN | ม.ค. | |
| FEB | ก.พ. | |
| MAR | มี.ค. | |
| APR | เม.ย. | |
| MAY | พ.ค. | |
| JUN | มิ.ย. | |
| JUL | ก.ค. | |
| AUG | ส.ค. | |
| SEP | ก.ย. | |
| OCT | ต.ค. | |
| NOV | พ.ย. | |
| DEC | ธ.ค. | |
| 2D graphics | กราฟิก 2D | "2D graphics, 16-bit color" = กราฟิก 2D สี 16 บิต |
| 3D graphics | กราฟิก 3D | |
| N-bit color | สี N บิต | Mega "2D 4 Bits" = 2D 4 บิต |
| monochrome / Monochromatic | โมโนโครม | |
| Voxel graphics | กราฟิกวอกเซล | |
| VR graphics | กราฟิก VR | |
| Augmented reality | ความจริงเสริม (AR) | |
| Virtual reality | ความจริงเสมือน (VR) | When spelled out; "VR" alone stays VR |
| High Definition | ความละเอียดสูง (HD) | |
| Ultra High Definition | ความละเอียดสูงพิเศษ (UHD) | |
| Mono sound | เสียงโมโน | |
| Stereo sound | เสียงสเตอริโอ | |
| Surround sound | เสียงเซอร์ราวด์ | |
| MIDI sound | เสียง MIDI | |
| Basic | พื้นฐาน | Tier word, placed after the noun: ดนตรีพื้นฐาน |
| Simple | แบบง่าย | Tier word: แอนิเมชันแบบง่าย |
| Advanced | ขั้นสูง | Tier word: ฟิสิกส์ขั้นสูง |
| Dynamic | ไดนามิก | แอนิเมชันไดนามิก |
| Interactive | อินเทอร์แอกทีฟ | บทสนทนาอินเทอร์แอกทีฟ; also the two "Interactive ..." genres |
| Orchestral music | ดนตรีออร์เคสตรา | |
| AI-based | ด้วย AI | "AI-based animation" = แอนิเมชันด้วย AI |
| AI-generated | สร้างด้วย AI | |
| AI-managed | คุมด้วย AI | |
| Saves | ระบบเซฟ | Engine features: "Basic saves" = ระบบเซฟพื้นฐาน |
| Password-based saves | เซฟด้วยรหัสผ่าน | |
| Cloud saves | เซฟบนคลาวด์ | |
| Cloud leaderboards | ตารางอันดับบนคลาวด์ | |
| Loading screen | หน้าโหลด | |
| Background loading | โหลดเบื้องหลัง | |
| Map editor | ตัวแก้ไขแผนที่ | |
| Gamepad | เกมแพด | "Gamepad support" = รองรับเกมแพด |
| Joystick | จอยสติ๊ก | |
| Mouse | เมาส์ | |
| Motion detection | ตรวจจับการเคลื่อนไหว | "Simple/Advanced motion detection" |
| Voice recognition | จดจำเสียง | |
| Facial recognition | จดจำใบหน้า | |
| Customizable characters | ตัวละครปรับแต่งได้ | |
| Prebuilt characters | ตัวละครสำเร็จรูป | |
| Realistic characters | ตัวละครสมจริง | |
| Social network integration | เชื่อมต่อโซเชียลมีเดีย | |
| Ragdolls | แร็กดอลล์ | Mega DLC |
| Censorship | เซนเซอร์ | Mega DLC |
| Cheat Code | สูตรโกง | Mega DLC |
| Controller Vibration | คอนโทรลเลอร์สั่น | Mega DLC |
| Parental Controls | ระบบควบคุมโดยผู้ปกครอง | Mega DLC |
| Dubbed | เสียงพากย์ | Mega DLC |
| Subtitles | ซับไตเติล | Mega DLC |
| Ray Tracing | เรย์เทรซิง | Mega DLC |
| Shaders | เชเดอร์ | Mega DLC |
| Skybox | สกายบ็อกซ์ | Mega DLC |
| Isometric | ไอโซเมตริก | Mega DLC |
| Gun Support | รองรับปืนแสง | Mega DLC |
| 4X | 4X | Genre (LABEL_TYPE_*); unchanged |
| Action | แอ็กชัน | Genre |
| Action-adventure | แอ็กชันผจญภัย | Genre |
| Action RPG | แอ็กชัน RPG | Genre |
| Adventure | ผจญภัย | Genre |
| Animals | สัตว์ | Genre |
| Artillery | ยิงปืนใหญ่ | Genre |
| Beat 'em up | บีตเอ็มอัป | Genre |
| Bishojo | บิโชโจะ | Genre |
| Breakout | เบรกเอาต์ | Genre |
| Casual | แคชชวล | Genre |
| Chat (LABEL_TYPE_CHAT) | จีบสาว | Genre; FR "Drague" = dating/flirting game, not chatting |
| City builder | สร้างเมือง | Genre |
| Clicker game | คลิกเกอร์ | Genre |
| Crook-like | Crook-like | Genre; parody name, unchanged |
| Driving | ขับรถ | Genre |
| Dungeon | ดันเจี้ยน | Genre; also Mega theme |
| Dungeon crawler | ตะลุยดันเจี้ยน | Genre |
| Economy | เศรษฐกิจ | Genre |
| Eroge | เอโรเกะ | Genre |
| Farming | ทำฟาร์ม | Genre |
| Flight | การบิน | Genre |
| FPS | FPS | Genre; unchanged ("Force 120 FPS" is frames per second, also unchanged) |
| God game | ก็อดเกม | Genre |
| Government | บริหารประเทศ | Genre |
| Hack'n'slash | แฮ็กแอนด์สแลช | Genre |
| Hidden objects | หาของ | Genre |
| Horror | สยองขวัญ | Genre and theme |
| HTA-like | HTA-like | Genre; parody name, unchanged |
| Infiltration | ลอบเร้น | Genre; Mega theme "Stealth" is the same word |
| Interactive fiction | นิยายอินเทอร์แอกทีฟ | Genre |
| Interactive movie | หนังอินเทอร์แอกทีฟ | Genre |
| Living organism | สิ่งมีชีวิต | Genre |
| Management | บริหารจัดการ | Genre |
| Maze | เขาวงกต | Genre; also Mega theme |
| MMO-RPG | MMO-RPG | Genre; unchanged |
| MOBA-like | MOBA-like | Genre; unchanged |
| Mystery-like | Mystery-like | Genre; parody name, unchanged |
| Open world | โอเพนเวิลด์ | Genre and engine feature |
| Otome | โอโตเมะ | Genre |
| Platforms (LABEL_TYPE_PLATFORMS) | แพลตฟอร์มเมอร์ | Genre (platformer), not hardware |
| Brain teaser | ลับสมอง | Genre (key LABEL_TYPE_PUZZLE, FR "Casse-tête") |
| Puzzle | พัซเซิล | Genre (key LABEL_TYPE_REFLEXION); also Mega theme |
| Racing | แข่งรถ | Genre |
| RPG | RPG | Genre; unchanged |
| RTS | RTS | Genre; unchanged |
| RTT | RTT | Genre; unchanged |
| Rhythm | ริทึม | Genre |
| Shoot | ชูตติ้ง | Genre |
| Shoot 'em up | ชูตเอ็มอัป | Genre |
| Simulation | ซิมูเลชัน | Genre |
| Space | อวกาศ | Genre; also Mega theme |
| Sport | กีฬา | Genre |
| Strategy | วางแผน | Genre. Outside genre names "strategy" = กลยุทธ์ |
| Submarine | เรือดำน้ำ | Genre |
| Survival | เอาชีวิตรอด | Genre |
| Tactical RPG | แทคติคัล RPG | Genre |
| Tower defense | ทาวเวอร์ดีเฟนส์ | Genre |
| TPS | TPS | Genre; unchanged |
| Train | รถไฟ | Genre |
| Turn-based | เทิร์นเบส | Genre |
| Vehicle | ยานพาหนะ | Genre |
| Versus fighting | ไฟติ้ง | Genre |
| Visual novel | วิชวลโนเวล | Genre |
| Sandbox | แซนด์บ็อกซ์ | Engine feature |
| Anime | อนิเมะ | Theme |
| Arabian Nights | อาหรับราตรี | Theme |
| Archeology | โบราณคดี | Theme |
| Atlantis | แอตแลนติส | Theme |
| Cartoon | การ์ตูน | Theme |
| Comedy | ตลก | Theme |
| Cooking | ทำอาหาร | Theme |
| Crossover | ครอสโอเวอร์ | Theme |
| Cyberpunk | ไซเบอร์พังก์ | Theme |
| Desert | ทะเลทราย | Theme |
| Dragon | มังกร | Theme |
| Erotic | อีโรติก | Theme |
| Evolution | วิวัฒนาการ | Theme |
| Fantasy | แฟนตาซี | Theme |
| Football | อเมริกันฟุตบอล | Theme; FR "Football américain". Mega "American Football" is the same |
| Soccer | ฟุตบอล | Theme |
| Game dev | ทำเกม | Theme |
| Ghost | ผี | Theme |
| History | ประวัติศาสตร์ | Theme |
| Hunt | ล่าสัตว์ | Theme |
| Industrialization | ยุคอุตสาหกรรม | Theme |
| Kaiju | ไคจู | Theme |
| Medical | การแพทย์ | Theme |
| Medieval | ยุคกลาง | Theme |
| Military | ทหาร | Theme |
| Movie adaptation | ดัดแปลงจากหนัง | Theme |
| Mythology | เทพปกรณัม | Theme |
| Ninja | นินจา | Theme |
| Ocean | มหาสมุทร | Theme |
| Organized crime | องค์กรอาชญากรรม | Theme |
| Park | สวนสนุก | Theme; FR "Parc de loisirs" |
| Pet | สัตว์เลี้ยง | Theme |
| Pirate | โจรสลัด | Theme |
| Post-apocalyptic | โลกหลังหายนะ | Theme |
| Prehistory | ยุคก่อนประวัติศาสตร์ | Theme |
| Religious | ศาสนา | Theme |
| Science fiction | ไซไฟ | Theme |
| Spy | สายลับ | Theme (the action "Spy on" is สอดแนม) |
| Steampunk | สตีมพังก์ | Theme |
| Superhero | ซูเปอร์ฮีโร่ | Theme |
| Time travel | ข้ามเวลา | Theme |
| Transportation | ขนส่ง | Theme |
| Urban | ชีวิตเมือง | Theme |
| Vampire | แวมไพร์ | Theme |
| Western | คาวบอย | Theme |
| Zombie | ซอมบี้ | Theme |
| Lovecraftian | เลิฟคราฟต์ | Mega theme |
| Looter Shooter | ลูตเตอร์ชูตเตอร์ | Mega theme |
| Mechs | หุ่นรบ | Mega theme |
| Mecha | เมชา | Mega theme; distinct from Mechs |
| Dark Fantasy | ดาร์กแฟนตาซี | Mega theme |
| Metroidvania | เมทรอยด์วาเนีย | Mega theme |
| Bullet Hell | บุลเล็ตเฮล | Mega theme |
| Souls Like | โซลไลก์ | Mega theme |
| Card Game | การ์ดเกม | Mega theme |
| Choices Matter | ทางเลือกมีผล | Mega theme |
| Walking Simulator | วอล์กกิงซิม | Mega theme |
| Colony Simumlator | โคโลนีซิม | Mega theme (source typo) |
| Arena Shooter | อารีนาชูตเตอร์ | Mega theme |
| Perma Death | ตายแล้วตายเลย | Mega theme |
| Stealth | ลอบเร้น | Mega theme |
| eSport | อีสปอร์ต | Mega theme |
| Shooter | ชูตเตอร์ | Mega theme |
| Demons | เหล่าปีศาจ | Mega theme; distinct from Demon |
| Demon | ปีศาจ | Mega theme |
| Bounty Hunter / Bountyhunter | นักล่าค่าหัว | Mega theme (two entries, same Thai) |
| Hacking | แฮ็กกิ้ง | Mega theme; base theme "Hack" stays แฮ็ก |
| Mutation | การกลายพันธุ์ | Mega theme |
| Mutant | มนุษย์กลายพันธุ์ | Mega theme |
| Rome | กรุงโรม | Mega theme |
| Roman Empire | จักรวรรดิโรมัน | Mega theme |
| Dating | เดต | Mega theme |
| Old School | โอลด์สคูล | Mega theme |
| I want more! | ขออีก! | Repeated achievement title; keep the source's number of "!" and add สิ for the ALL-CAPS variant (ขออีกสิ!) |
| It is alive! ALIVE! | มันมีชีวิต! มีชีวิตแล้ว! | Repeated achievement title (Frankenstein) |
| Create a famous game | สร้างเกมดัง | Repeated achievement description |
| Let's create a new game! | มาสร้างเกมใหม่กัน! | Repeated achievement title |
| Create a game engine | สร้างเอนจิน | Repeated achievement description |
| The Cellar Player | เกมเมอร์ห้องใต้ดิน | Fan-mail signature; translated as a nickname |
| University of Mars | มหาวิทยาลัยดาวอังคาร | Joke in the job-application mail |
| The department of bad sales | แผนกยอดขายแย่ | Running joke; same wording in the mail and the loading tip |
| Santa | ซานต้า | Mega DLC events |

## Do not translate

Keep these exactly as in the source (Latin script, same spelling and capitalisation):

- **The game and its developer:** City Game Studio, CGS MEGA DLC, Magazines DLC, Supporter Pack, Binogure, BinoPal, Einstein (the mascot dog), Sneak In.
- **Fictional companies and hardware:** Grantendo, Super Grantendo, Super GES, GameStation, Deny, Moris, Saga, Saga VR, Wataggi, Plastics, Roberto Industries, RobertoVision, Joycast, DustStar, Blue Studio, Kryzon Studios. Every other console, component, manufacturer and rival-studio name delivered through %s is left untouched as well.
- **Fictional people, shows and press:** Gio Tard, Rock Paper Pistol, Bruno Trigger, 3615 Dorian, Dorian, The Smitties, Rick, Paris; magazines Fan Game, PC Player, Game Geek, Game over Mag, Geek Hub, Game 2, ZQSD, Wiki Player, Godot Mania.
- **Real brands, services and tech:** Steam, Steam Workshop, Twitch, Discord, Cloudflare, Game Pass, Xbox Game Pass, Xbox Series, Playstation 5, Bethesda, Starfield, Tesla, Dolby Vision, G Sync, VRR, Nanite, NASCAR, Formula 1, Black Friday, HTTP/3, DDoS, CDN, WAF, PCI, TLS.
- **Real people:** Elon Musk, Todd Howard, Susan Boyle, Wayne Rooney. Mod credits: handa.aadit14, Sicko on Series X #7196, GianluPlay, Diminatsis.
- **Franchise names used as themes or references:** World of Warcraft, Lord of the Rings, Warhammer, Star Wars, Starcraft, Star Trek, ET (the 1982 game), Wololo, Veni vidi vici, Friendslop, Solari.
- **Abbreviations and technical tokens:** CPU, GPU, RAM, MMO, RPG, FPS, TPS, RTS, RTT, 4X, MOBA, DLC, DRM, AAA, 2D, 2.5D, 3D, VR, AR, HD, UHD, 8K, AI, UI, API, SDK, HR, CEO, QA, IP, FOSS, GOTY, MIDI, ASCII, VSync, CD-ROM, PC, F1 (the key), ULTD, World PRO, World MAX, LGBT.
- **Easing names (LABEL_TRANS_*):** Back, Bounce, Circ, Cubic, Elastic, Expo, Linear, Quad, Quart, Quint, Sine.
- **Number suffix letters (LABEL_UNIT_*):** K, M, G, T, P, E, Z, Y.
- **Identifiers that are not text:** any value in CAPS_WITH_UNDERSCORES (LABEL_DESCRIPTION_17, BUTTON_EVENT_CUSTOM_0 ...) and the Mega DLC theme IDs beginning FN3-, F3-, FN9-, fn9-, fn-9, fn9_ (for example FN3-Lovecraftian, fn9_bomb): output unchanged.
- **URLs, res:// paths, BBCode tags, %-placeholders and [square]/{curly} tokens** such as [player_name] and [studio_name].

Translated, not kept (so they read naturally): country names (USA = สหรัฐอเมริกา, China = จีน, North Korea = เกาหลีเหนือ, Brasil = บราซิล, Argentina = อาร์เจนตินา, Mexico = เม็กซิโก, Russia = รัสเซีย, Ukraine = ยูเครน), Covid 19 = โควิด-19, Monalisa = โมนาลิซา, Christmas = คริสต์มาส.
