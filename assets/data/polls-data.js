/* 33-Year Presidential Polls Animation & Current Term Trajectory */
    let pollAnimTimer = null;
    let pollAnimStep = 0;
    const POLL_PRESIDENTS_DATA = [
      { name: "노태우 정부 (1988~1993)", color: "#A855F7", start: 29, high: 57, end: 12, milestone: "1988 서울올림픽 57% ➔ 북방외교 ➔ 1992 퇴임기 12%" },
      { name: "김영삼 정부 (1993~1998)", color: "#3B82F6", start: 83, high: 83, end: 6, milestone: "1993 금융실명제 83% 역대 최고 ➔ 1997 외환위기 IMF 6% 최저" },
      { name: "김대중 정부 (1998~2003)", color: "#10B981", start: 71, high: 71, end: 24, milestone: "1998 IMF 극복 71% ➔ 2000 남북정상회담 68% ➔ 카드사태 24%" },
      { name: "노무현 정부 (2003~2008)", color: "#EAB308", start: 60, high: 60, end: 27, milestone: "2003 취임 60% ➔ 2004 탄핵기각 40% ➔ 부동산 폭등 12% ➔ FTA 27%" },
      { name: "이명박 정부 (2008~2013)", color: "#06B6D4", start: 52, high: 52, end: 24, milestone: "2008 취임 52% ➔ 광우병 촛불 21% ➔ 글로벌 금융위기 극복 44% ➔ 24%" },
      { name: "박근혜 정부 (2013~2016)", color: "#EC4899", start: 54, high: 54, end: 5, milestone: "2013 취임 54% ➔ 세월호 40% ➔ 메르스 33% ➔ 2016 국정농단 탄핵 5%" },
      { name: "문재인 정부 (2017~2022)", color: "#3B82F6", start: 84, high: 84, end: 45, milestone: "2017 취임 84% ➔ 평양 남북정상회담 83% ➔ 코로나 대응 71% ➔ 퇴임 45%" },
      { name: "윤석열 정부 (2022~2026)", color: "#EF4444", start: 52, high: 52, end: 21, milestone: "2022 취임 52% ➔ 순방 24% ➔ 2024 총선 23% ➔ 2026.10 현재 21% 공방" }
    ];

    function togglePresidentsPollAnimation() {
      const btn = document.getElementById('pollAnimPlayBtn');
      if (pollAnimTimer) {
        clearInterval(pollAnimTimer);
        pollAnimTimer = null;
        if (btn) btn.innerHTML = '<span>▶️ 33년 정권 궤적 순차 재생</span>';
      } else {
        pollAnimStep = 0;
        if (btn) btn.innerHTML = '<span>⏸️ 일시 정지</span>';
        stepPresidentsPollAnimation();
        pollAnimTimer = setInterval(stepPresidentsPollAnimation, 1800);
      }
    }

    function stepPresidentsPollAnimation() {
      const badge = document.getElementById('pollAnimStatusBadge');
      if (pollAnimStep >= POLL_PRESIDENTS_DATA.length) {
        clearInterval(pollAnimTimer);
        pollAnimTimer = null;
        const btn = document.getElementById('pollAnimPlayBtn');
        if (btn) btn.innerHTML = '<span>🔄 처음부터 다시 재생</span>';
        resetPresidentsPollAnimation(true);
        if (badge) badge.innerHTML = '🎉 <strong>33개년 8대 정권 전체 비교 궤적 완성!</strong>';
        return;
      }

      const p = POLL_PRESIDENTS_DATA[pollAnimStep];
      if (badge) {
        badge.innerHTML = `<span style="color:${p.color};">●</span> <strong>[${pollAnimStep + 1}/8] ${p.name}:</strong> ${p.milestone}`;
      }

      // Draw single president on chart
      renderAnimatedPollStep(pollAnimStep);
      pollAnimStep++;
    }

    function resetPresidentsPollAnimation(showAll = false) {
      if (pollAnimTimer) {
        clearInterval(pollAnimTimer);
        pollAnimTimer = null;
      }
      const btn = document.getElementById('pollAnimPlayBtn');
      if (btn) btn.innerHTML = '<span>▶️ 33년 정권 궤적 순차 재생</span>';
      switchHistoricalPollView('presidents');
    }

    function renderAnimatedPollStep(step) {
      const p = POLL_PRESIDENTS_DATA[step];
      const box = document.getElementById('historicalPollContentBox');
      if (!box) return;
      
      // Highlight card and show dynamic SVG trajectory
      box.innerHTML = `
        <div style="background: rgba(15, 23, 42, 0.7); border: 2px solid ${p.color}; border-radius: 16px; padding: 24px; box-shadow: 0 0 30px ${p.color}44;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div>
              <span style="font-size: 0.8rem; font-weight: 800; color: ${p.color}; background: ${p.color}22; padding: 3px 10px; border-radius: 6px;">STEP ${step + 1} / 8</span>
              <h3 style="font-size: 1.45rem; font-weight: 800; color: #F8FAFC; margin: 6px 0 2px 0;">${p.name}</h3>
              <div style="font-size: 0.85rem; color: #94A3B8;">${p.milestone}</div>
            </div>
            <div style="text-align: right;">
              <div style="font-size: 0.8rem; color: #86868B;">최고 ➔ 최저 궤적</div>
              <div style="font-size: 1.7rem; font-weight: 900; color: ${p.color};">${p.high}% ➔ ${p.end}%</div>
            </div>
          </div>

          <!-- Dynamic SVG Line for this Presidency -->
          <div style="background: #070B14; border-radius: 12px; padding: 18px; border: 1px solid rgba(255,255,255,0.08);">
            <svg viewBox="0 0 800 220" style="width: 100%; height: 180px; overflow: visible;">
              <!-- Grid lines -->
              <line x1="40" y1="20" x2="780" y2="20" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
              <line x1="40" y1="80" x2="780" y2="80" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
              <line x1="40" y1="140" x2="780" y2="140" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4 4" />
              <line x1="40" y1="200" x2="780" y2="200" stroke="rgba(255,255,255,0.15)" />
              
              <!-- Labels -->
              <text x="25" y="24" fill="#64748B" font-size="11" text-anchor="end">80%</text>
              <text x="25" y="84" fill="#64748B" font-size="11" text-anchor="end">50%</text>
              <text x="25" y="144" fill="#64748B" font-size="11" text-anchor="end">20%</text>
              <text x="25" y="204" fill="#64748B" font-size="11" text-anchor="end">0%</text>

              <!-- Animated Trajectory Line -->
              <path d="M 60 ${200 - p.start * 2.2} Q 240 ${200 - p.high * 2.2} 480 ${200 - ((p.start+p.end)/2) * 2.2} T 760 ${200 - p.end * 2.2}" 
                    fill="none" stroke="${p.color}" stroke-width="4.5" stroke-linecap="round" />
              
              <!-- Points -->
              <circle cx="60" cy="${200 - p.start * 2.2}" r="7" fill="${p.color}" />
              <text x="60" y="${200 - p.start * 2.2 - 12}" fill="#FFF" font-size="12" font-weight="700" text-anchor="middle">취임 ${p.start}%</text>

              <circle cx="760" cy="${200 - p.end * 2.2}" r="7" fill="${p.color}" />
              <text x="760" y="${200 - p.end * 2.2 - 12}" fill="#FFF" font-size="12" font-weight="700" text-anchor="middle">퇴임/현재 ${p.end}%</text>
            </svg>
          </div>
        </div>
      `;
    }

    // 4 Polls Scrubber Trajectory
    const FOUR_POLLS_HISTORY = [
      { date: "2022.05 (취임)", nbs: [52, 34], gallup: [52, 37], realm: [52.1, 40.6], mbc: [51.8, 38.2] },
      { date: "2023.04 (방미)", nbs: [30, 60], gallup: [30, 63], realm: [34.5, 62.6], mbc: [32.1, 61.4] },
      { date: "2024.04 (총선)", nbs: [27, 64], gallup: [23, 68], realm: [32.3, 64.3], mbc: [26.4, 66.8] },
      { date: "2025.04 (4년차)", nbs: [25, 66], gallup: [20, 71], realm: [26.8, 69.2], mbc: [23.5, 68.9] },
      { date: "2026.10 (현재)", nbs: [28, 64], gallup: [22, 69], realm: [24.6, 71.4], mbc: [24.8, 68.2] }
    ];

    function setPresidentTermPoint(idx) {
      renderFourPollsChart(idx);
      document.querySelectorAll('.poll-time-pill').forEach((btn, i) => {
        btn.classList.toggle('active', i === idx);
        if (i === idx) {
          btn.style.background = '#2997FF';
          btn.style.color = '#FFF';
          btn.style.fontWeight = '700';
          btn.style.border = 'none';
        } else {
          btn.style.background = 'rgba(255,255,255,0.06)';
          btn.style.color = '#94A3B8';
          btn.style.fontWeight = 'normal';
          btn.style.border = '1px solid rgba(255,255,255,0.12)';
        }
      });

      const data = FOUR_POLLS_HISTORY[idx];
      const grid = document.getElementById('fourPollsGridContainer');
      if (!grid) return;
      
      // Update values dynamically with animation
      const cards = grid.children;
      if (cards.length >= 4) {
        updatePollCardVal(cards[0], "NBS 전국지표조사", data.nbs, data.date);
        updatePollCardVal(cards[1], "한국갤럽", data.gallup, data.date);
        updatePollCardVal(cards[2], "리얼미터", data.realm, data.date);
        updatePollCardVal(cards[3], "MBC 여론M", data.mbc, data.date);
      }
    }

    function updatePollCardVal(card, title, vals, dateLabel) {
      const posVal = card.querySelector('[style*="font-size: 1.85rem"]');
      const negVal = card.querySelectorAll('[style*="font-size: 1.85rem"]')[1];
      const ratioBars = card.querySelectorAll('[style*="background: #2997FF"], [style*="background: #FF453A"]');
      
      if (posVal) posVal.innerHTML = `${vals[0]}<span style="font-size: 1rem; font-weight: 700;">%</span>`;
      if (negVal) negVal.innerHTML = `${vals[1]}<span style="font-size: 1rem; font-weight: 700;">%</span>`;
      
      if (ratioBars && ratioBars.length >= 2) {
        ratioBars[0].style.transition = 'width 0.4s ease';
        ratioBars[0].style.width = vals[0] + '%';
        ratioBars[1].style.transition = 'width 0.4s ease';
        ratioBars[1].style.width = vals[1] + '%';
      }
    }

    function playPresidentTrajectory() {
      let i = 0;
      const interval = setInterval(() => {
        setPresidentTermPoint(i);
        i++;
        if (i >= (window.INFLECTION_EVENTS_DATA ? window.INFLECTION_EVENTS_DATA.length : FOUR_POLLS_HISTORY.length)) {
          clearInterval(interval);
        }
      }, 700);
    }

    async function copyKakaoIdAndOpen() {
      try {await navigator.clipboard.writeText('youngsun1976');alert('카카오톡 ID를 복사했습니다. 카카오톡의 친구 추가 > ID로 추가에서 검색할 수 있습니다. ID 검색 허용 여부에 따라 검색되지 않을 수 있으며, 이 버튼은 대화방을 직접 열지 않습니다.');}
      catch(e){alert('카카오톡 ID: youngsun1976. 직접 복사하여 사용하세요.');}
    }

    // =========================================================================
    // 📈 현 정권 4대 조사 인터랙티브 SVG 시계열 그래프 & 변곡점 심층 팝업 엔진 (v2026.10.30)
    // =========================================================================
    
    // 5대 핵심 변곡점 심층 팩트체크 데이터베이스
    window.INFLECTION_EVENTS_DATA = [
  {
    "idx": 0,
    "date": "2022.05 (취임 & 청와대 개방)",
    "shortLabel": "22.05 취임",
    "period": "제20대 대통령 취임 및 정부 출범 초기",
    "approval": {
      "nbs": [
        52,
        34
      ],
      "gallup": [
        52,
        37
      ],
      "realm": [
        52.1,
        40.6
      ],
      "mbc": [
        51.8,
        38.2
      ],
      "avgPos": 52.0,
      "avgNeg": 37.5
    },
    "videoId": "4LSmiA4rlHg",
    "videoTitle": "윤석열 대통령 취임식 및 74년 만의 청와대 전면 개방",
    "events": [
      {
        "tag": "정부 출범",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "제20대 대통령 취임식 및 74년 만의 청와대 전면 개방",
        "desc": "청와대 국민 개방과 함께 국방부 청사로 대통령실을 전격 이전하며 용산 시대를 개막."
      },
      {
        "tag": "외교 안보",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "취임 11일 만의 한미정상회담 (조 바이든 미국 대통령 방한)",
        "desc": "역대 최단기 한미정상회담을 통해 한미동맹을 군사안보를 넘어 기술·공급망 포괄 전략동맹으로 격상."
      },
      {
        "tag": "지방 선거",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "제8회 전국동시지방선거 국민의힘 압승",
        "desc": "광역단체장 17곳 중 12곳을 여당이 석권하며 정권 초기 강력한 국정 드라이브 동력을 확보."
      }
    ],
    "partySupport": "국민의힘 43~45% vs 더불어민주당 30~32%",
    "analysis": "정권 교체 열망과 전통적 허니문(Honeymoon) 효과가 결합되어 임기 중 최고 지지율(52~53%)을 기록함. 그러나 집무실 이전 논란과 1기 내각 인사 청문 잡음이 초기 불안 요인으로 잠복함."
  },
  {
    "idx": 1,
    "date": "2022.08 (집중호우 & 펠로시 의전 논란)",
    "shortLabel": "22.08 펠로시",
    "period": "집권 1년차 여름 첫 지지율 20%대 급락",
    "approval": {
      "nbs": [
        28,
        65
      ],
      "gallup": [
        24,
        66
      ],
      "realm": [
        29.3,
        67.8
      ],
      "mbc": [
        27.2,
        66.4
      ],
      "avgPos": 27.1,
      "avgNeg": 66.4
    },
    "videoId": "BIBJI1mKcKw",
    "videoTitle": "낸시 펠로시 미 하원의장 방한 의전 논란 및 수도권 집중호우 대처",
    "events": [
      {
        "tag": "외교 의전",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "낸시 펠로시 미국 하원의장 방한 의전 결례 논란",
        "desc": "대통령 여름휴가 일정과 겹쳐 면담 대신 전화 통화로 대체되며 외교가와 여론의 거센 의전 비판 직면."
      },
      {
        "tag": "재난 대처",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "중부권 115년 만의 기록적 집중호우 및 반지하 침수 참사",
        "desc": "대통령 자택 원격 지휘 논란 속 국가 위기관리 컨트롤타워 부재에 대한 여론의 강한 질타."
      },
      {
        "tag": "당내 갈등",
        "tagBg": "rgba(191, 90, 242, 0.15)",
        "tagColor": "#BF5AF2",
        "title": "이준석 대표 당원권 정지 중징계 및 '내부총질' 문자 유출",
        "desc": "권성동 원내대표와의 텔레그램 문자 유출로 여권 내홍이 최고조에 달하며 2030 청년 보수층 급격 이탈."
      }
    ],
    "partySupport": "국민의힘 34~36% vs 더불어민주당 36~38%",
    "analysis": "취임 100일도 채 되지 않아 한국갤럽 기준 24%로 급락하며 첫 지지율 위기 봉착. 인사·재난·외교 악재가 연쇄 폭발하며 긍·부정 평가 데드크로스가 -40%p 가까이 벌어짐."
  },
  {
    "idx": 2,
    "date": "2022.09 (뉴욕 순방 비속어 논란)",
    "shortLabel": "22.09 비속어",
    "period": "집권 1년차 가을 한미·한일 외교전과 언론 격돌",
    "approval": {
      "nbs": [
        31,
        60
      ],
      "gallup": [
        28,
        65
      ],
      "realm": [
        31.2,
        66.0
      ],
      "mbc": [
        30.1,
        63.8
      ],
      "avgPos": 30.1,
      "avgNeg": 63.7
    },
    "videoId": "b95KHYSVI_8",
    "videoTitle": "뉴욕 글로벌펀드 순방 비속어 논란 및 바이든/날리면 공방",
    "events": [
      {
        "tag": "외교 파문",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "뉴욕 글로벌 펀드 회의장 퇴장 시 비속어 발언 논란",
        "desc": "‘국회에서 이 XX들이 승인 안 해주면... 바이든/날리면’ 발언 진위 공방으로 외교 성과가 완전 매몰."
      },
      {
        "tag": "언론 갈등",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "대통령실의 MBC 전용기 탑승 배제 통보",
        "desc": "취재 편의 제한 조치로 언론계와 야권의 탄압 반발 확산, 국정 소통 방식에 대한 부정 여론 증폭."
      },
      {
        "tag": "영빈관 논란",
        "tagBg": "rgba(191, 90, 242, 0.15)",
        "tagColor": "#BF5AF2",
        "title": "878억 원 규모 영빈관 신축 예산 편성 및 하루 만의 철회",
        "desc": "용산 이전 비용 논란 재점화로 중도층의 예산 우선순위 불신 가중."
      }
    ],
    "partySupport": "국민의힘 32~34% vs 더불어민주당 35~37%",
    "analysis": "순방 외교가 국정 지지율의 반등 지렛대가 되지 못하고 오히려 여야 극한 대치의 촉매제가 됨. 부정 평가 요인 중 '말실수·소통 미흡'이 1위로 부상."
  },
  {
    "idx": 3,
    "date": "2022.10 (이태원 10·29 참사)",
    "shortLabel": "22.10 이태원",
    "period": "집권 1년차 말 국가적 비극과 안전 시스템 검증",
    "approval": {
      "nbs": [
        31,
        62
      ],
      "gallup": [
        29,
        62
      ],
      "realm": [
        34.2,
        63.8
      ],
      "mbc": [
        31.5,
        62.9
      ],
      "avgPos": 31.4,
      "avgNeg": 62.7
    },
    "videoId": "PPSQByrQpHE",
    "videoTitle": "이태원 10·29 참사 발생 및 일주일간 국가애도기간 선포",
    "events": [
      {
        "tag": "국가 재난",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "이태원 할로윈 압사 참사로 159명 희생",
        "desc": "도심 한복판에서 벌어진 대형 인명 피해로 국가 안전관리 시스템의 총체적 마비 확인."
      },
      {
        "tag": "책임 공방",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "이상민 행정안전부 장관 문책 공방 및 국회 탄핵안 발의",
        "desc": "정치적·도의적 책임론을 둘러싼 정쟁 격화 속 야당 주도의 장관 해임건의안 및 탄핵소추 가결."
      },
      {
        "tag": "국가 애도",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "대통령의 합동분향소 연일 조문 및 국가애도기간 선포",
        "desc": "추모 분위기 속에서도 책임자 처벌 및 재발 방지 대책을 둘러싼 사회적 갈등 장기화."
      }
    ],
    "partySupport": "국민의힘 32~34% vs 더불어민주당 34~36%",
    "analysis": "슬픔과 충격 속에서 국민적 불안감이 극에 달함. 정부의 초기 대응과 사후 수습 방식을 둘러싼 불만이 부정 평가를 60%대 초반에 견고히 고착화시킴."
  },
  {
    "idx": 4,
    "date": "2022.12 (화물연대 업무개시명령 반등)",
    "shortLabel": "22.12 화물연대",
    "period": "집권 1년차 결산 및 법과 원칙 드라이브",
    "approval": {
      "nbs": [
        34,
        56
      ],
      "gallup": [
        36,
        56
      ],
      "realm": [
        39.5,
        57.3
      ],
      "mbc": [
        36.8,
        56.5
      ],
      "avgPos": 36.7,
      "avgNeg": 56.5
    },
    "videoId": "N_UCqhwar7Q",
    "videoTitle": "민주노총 화물연대 집단운송거부 사태에 사상 첫 업무개시명령 발동",
    "events": [
      {
        "tag": "법치 원칙",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "화물연대 집단운송거부에 사상 첫 시멘트·철강 업무개시명령",
        "desc": "불법 파업에 타협 없다는 단호한 '법과 원칙' 기조를 관철하며 물류 정상화 조기 달성."
      },
      {
        "tag": "노동 개혁",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "3대 개혁(노동·교육·연금) 드라이브 본격 선언",
        "desc": "노조 회계 투명성 제고 및 건폭(건설현장 폭력) 근절 기조를 천명하며 국정 어젠다 주도권 확보."
      },
      {
        "tag": "보수 결집",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "지지율 40%선 돌파 육박 및 당정 장악력 강화",
        "desc": "단호한 결단력에 호응한 전통 보수층과 영남권 지지층이 전면 재결집."
      }
    ],
    "partySupport": "국민의힘 36~38% vs 더불어민주당 32~34%",
    "analysis": "취임 후 가장 강력한 지지율 반등 국면. 리얼미터 기준 40%선에 육박하며 출범 이래 최고 회복세를 보임. 원칙 중심의 강한 리더십이 보수층의 강력한 효능감을 자극함."
  },
  {
    "idx": 5,
    "date": "2023.03 (일제 강제동원 제3자 변제)",
    "shortLabel": "23.03 강제동원",
    "period": "집권 2년차 전반기 한일관계 전격 복원",
    "approval": {
      "nbs": [
        33,
        60
      ],
      "gallup": [
        34,
        58
      ],
      "realm": [
        36.7,
        60.4
      ],
      "mbc": [
        34.5,
        59.8
      ],
      "avgPos": 34.7,
      "avgNeg": 59.6
    },
    "videoId": "V0fD2Yods0k",
    "videoTitle": "일제 강제동원 피해자 제3자 변제 해법 발표 및 한일 셔틀외교 복원",
    "events": [
      {
        "tag": "외교 결단",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "일제 강제징용 대법 판결에 '제3자 변제' 해법 공식 발표",
        "desc": "국내 재단이 배상금을 대신 변제하는 파격 결단으로 경색된 한일관계의 전격 돌파구 마련."
      },
      {
        "tag": "정상 외교",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "12년 만의 한일 정상회담 및 셔틀외교 재개",
        "desc": "도쿄에서 기시다 후미오 총리와 회담하며 일본의 반도체 소재 수출규제 해제 및 화이트리스트 복원."
      },
      {
        "tag": "국내 반발",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "야권과 시민단체의 '굴욕 외교' 대규모 장외 투쟁",
        "desc": "피해자 동의 없는 일방적 양보라는 비판과 함께 정치권 역사 공방이 전면 격화."
      }
    ],
    "partySupport": "국민의힘 34~36% vs 더불어민주당 33~35%",
    "analysis": "외교적 미래지향성 강조 vs 역사적 굴욕 프레임이 첨예하게 대립. 보수층은 한미일 공조 복원으로 평가했으나 중도층과 호남권의 강한 반발로 부정 평가가 다시 60%선을 위협함."
  },
  {
    "idx": 6,
    "date": "2023.04 (미국 국빈 방문 & 워싱턴 선언)",
    "shortLabel": "23.04 방미",
    "period": "집권 2년차 전반기 글로벌 중추국가 외교",
    "approval": {
      "nbs": [
        30,
        60
      ],
      "gallup": [
        30,
        63
      ],
      "realm": [
        34.5,
        62.6
      ],
      "mbc": [
        32.1,
        61.4
      ],
      "avgPos": 31.7,
      "avgNeg": 61.8
    },
    "videoId": "B3fMMaGdtWk",
    "videoTitle": "윤석열 대통령 미국 국빈 방문 및 미 상·하원 합동연설",
    "events": [
      {
        "tag": "동맹 격상",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "워싱턴 선언(Washington Declaration) 채택 및 NCG 신설",
        "desc": "한미 핵협의그룹(NCG) 창설을 통해 미국의 확장억제 공약을 제도적 실행 단계로 격상."
      },
      {
        "tag": "의회 연설",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "미 상·하원 합동 의회 영어 연설 및 국빈 만찬 아메리칸 파이 열창",
        "desc": "자유의 동맹 70주년을 역설하며 기립 박수를 이끌어내고 미국 조야의 폭발적 호응 유도."
      },
      {
        "tag": "경제 통상",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "59억 달러 대미 투자 유치 및 반도체·배터리 보조금 조율",
        "desc": "넷플릭스 25억 달러 투자 등 첨단 테크 수주 성과 달성."
      }
    ],
    "partySupport": "국민의힘 34~35% vs 더불어민주당 33~35%",
    "analysis": "국빈 방미 외교 성과로 지지율 낙폭을 방어하고 30%대 초반 지지선을 유지함. 그러나 러시아·중국과의 외교적 긴장감 고조와 민생 경기 둔화 우려가 병존함."
  },
  {
    "idx": 7,
    "date": "2023.08 (캠프 데이비드 한미일 정상회의)",
    "shortLabel": "23.08 캠프데이비드",
    "period": "집권 2년차 하반기 인도-태평양 전략 안착",
    "approval": {
      "nbs": [
        38,
        54
      ],
      "gallup": [
        34,
        57
      ],
      "realm": [
        37.6,
        59.4
      ],
      "mbc": [
        36.2,
        57.1
      ],
      "avgPos": 36.5,
      "avgNeg": 56.9
    },
    "videoId": "0BPAHZuY--Q",
    "videoTitle": "캠프 데이비드 한미일 3국 정상회의 출국 및 3자 협력 제도화",
    "events": [
      {
        "tag": "삼각 동맹",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "캠프 데이비드 3국 정상회의 원칙·정신·공약 채택",
        "desc": "단독 다자회의가 아닌 한미일 최초 단독 정상회의 개최로 3각 안보협력 협의체 영구 제도화."
      },
      {
        "tag": "안보 협력",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "북핵 미사일 경보정보 실시간 공유 체계 구축",
        "desc": "3국 연례 합동 군사훈련 정례화 및 공급망 조기경보시스템(EWS) 연계."
      },
      {
        "tag": "오염수 논란",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "일본 후쿠시마 원전 오염수 해양 방류 개시",
        "desc": "국내 수산물 안전 공방과 야당의 장외 총력 규탄 집회로 사회적 갈등 고조."
      }
    ],
    "partySupport": "국민의힘 36~37% vs 더불어민주당 31~33%",
    "analysis": "외교·안보 성과가 돋보이며 지지율이 30%대 후반(NBS 38%, 리얼 37.6%)으로 반등. 한미일 가치 외교의 결실로 평가받으며 중도 안보 보수층을 흡수함."
  },
  {
    "idx": 8,
    "date": "2023.10 (서울 강서구청장 보궐선거 대패)",
    "shortLabel": "23.10 강서보선",
    "period": "총선 D-6개월 수도권 민심의 경고",
    "approval": {
      "nbs": [
        31,
        61
      ],
      "gallup": [
        30,
        61
      ],
      "realm": [
        32.5,
        64.1
      ],
      "mbc": [
        31.4,
        62.0
      ],
      "avgPos": 31.2,
      "avgNeg": 62.0
    },
    "videoId": "WbZ7kBDLtKc",
    "videoTitle": "서울 강서구청장 보궐선거 여당 17.15%p 차 대패 및 혁신위 발족",
    "events": [
      {
        "tag": "선거 참패",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "10·11 강서구청장 보궐선거 여당 17.15%p 격차 참패",
        "desc": "사면 복권된 김태우 후보 공천 강행 후 대패하며 수도권 위기론이 거대한 실체로 확인."
      },
      {
        "tag": "당 쇄신",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "인요한 혁신위원회 출범 및 지도부·중진 험지 출마 요구",
        "desc": "당 주류 영남 중진들의 희생을 요구했으나 당내 기득권 반발로 혁신위 조기 좌초."
      },
      {
        "tag": "국정 기조",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "대통령의 '국민은 늘 무조건 옳다' 반성 메시지",
        "desc": "소통 강화와 서민 민생 행보(타운홀 미팅)로 전환을 시도했으나 정책 효과 체감 지연."
      }
    ],
    "partySupport": "국민의힘 33~35% vs 더불어민주당 36~38%",
    "analysis": "총선 전초전에서 수도권 민심의 거센 심판을 받으며 당정 일체화 드라이브에 치명상. 지지율은 다시 30%대 턱걸이로 주저앉았으며 당내 리더십 위기 가속화."
  },
  {
    "idx": 9,
    "date": "2024.01 (김건희 여사 특검법 거부권)",
    "shortLabel": "24.01 특검거부",
    "period": "총선 직전 정치 사법 리스크 최고조",
    "approval": {
      "nbs": [
        32,
        61
      ],
      "gallup": [
        31,
        63
      ],
      "realm": [
        35.7,
        61.2
      ],
      "mbc": [
        33.0,
        61.8
      ],
      "avgPos": 32.9,
      "avgNeg": 61.8
    },
    "videoId": "NZqEW8UBZXo",
    "videoTitle": "윤석열 대통령, '김건희 여사 특검법' 재의요구권(거부권) 행사",
    "events": [
      {
        "tag": "거부권 행사",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "김건희 여사 도이치모터스 & 대장동 50억 클럽 '쌍특검법' 거부권",
        "desc": "국회 통과 8일 만에 거부권을 행사하며 야당의 '가족 방탄용 특검 거부' 총공세 촉발."
      },
      {
        "tag": "의혹 파문",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "디올백 명품가방 수수 영상 공개 파문",
        "desc": "몰카 공작 논란 속에서도 영부인 리스크 관리를 위한 제2부속실 설치 및 특별감찰관 요구 비등."
      },
      {
        "tag": "당정 충돌",
        "tagBg": "rgba(191, 90, 242, 0.15)",
        "tagColor": "#BF5AF2",
        "title": "한동훈 비대위아카이브 사퇴 요구 및 서천 화재 현장 극적 봉합",
        "desc": "김경율 비대위원의 마리 앙투아네트 발언으로 대통령실과 한동훈 지도부 1차 정면충돌."
      }
    ],
    "partySupport": "국민의힘 36~38% vs 더불어민주당 34~36%",
    "analysis": "사법 리스크가 여론을 강타했으나 한동훈 비대위 출범 컨벤션 효과로 여당 지지율은 일시 버팀목을 형성. 그러나 특검 거부권에 대한 부정 여론(65% 상회)이 잠복."
  },
  {
    "idx": 10,
    "date": "2024.02 (의대 정원 2,000명 증원 발표)",
    "shortLabel": "24.02 의대증원",
    "period": "총선 2달 전 국정 지지율 일시적 급반등",
    "approval": {
      "nbs": [
        38,
        53
      ],
      "gallup": [
        39,
        53
      ],
      "realm": [
        41.1,
        55.4
      ],
      "mbc": [
        39.5,
        53.8
      ],
      "avgPos": 39.4,
      "avgNeg": 53.8
    },
    "videoId": "t9y4lpeMxGU",
    "videoTitle": "2025학년도 의과대학 입학정원 2,000명 파격 증원 발표",
    "events": [
      {
        "tag": "의료 개혁",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "2025학년도 의대 정원 2,000명 파격 증원 전격 발표",
        "desc": "27년 만의 의대 정원 확대로 필수의료 및 지역의료 살리기 개혁 청사진 제시."
      },
      {
        "tag": "의료계 반발",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "전국 전공의 1만여 명 집단 사직 및 의대생 동맹휴학",
        "desc": "면허정지 행정처분 예고와 정부 강경 대응 속 대학병원 응급실·수술실 셧다운 위기 확산."
      },
      {
        "tag": "여론 호응",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "한국갤럽 39%, 리얼미터 41.1%로 지지율 깜짝 반등",
        "desc": "의대 증원에 대한 70~80% 압도적 찬성 여론에 힘입어 1년 만에 지지율 40%선 재탈환."
      }
    ],
    "partySupport": "국민의힘 37~40% vs 더불어민주당 33~36%",
    "analysis": "개혁 과제에 대한 국민적 공감대가 폭발하며 총선 승리 기대감이 최고조로 고조됨. 그러나 사태 장기화에 대한 출구 전략 부재가 향후 메가톤급 부메랑으로 작동."
  },
  {
    "idx": 11,
    "date": "2024.04 (제22대 총선 여당 108석 참패)",
    "shortLabel": "24.04 총선참패",
    "period": "총선 심판과 레임덕 위기 현실화",
    "approval": {
      "nbs": [
        27,
        64
      ],
      "gallup": [
        23,
        68
      ],
      "realm": [
        32.3,
        64.3
      ],
      "mbc": [
        26.4,
        66.8
      ],
      "avgPos": 27.2,
      "avgNeg": 65.9
    },
    "videoId": "8N2lDatCUjY",
    "videoTitle": "4·10 제22대 총선 개표 결과: 범야권 압승 및 정권 심판",
    "events": [
      {
        "tag": "선거 참패",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "4·10 총선 여당 108석 vs 범야권 192석 압도적 참패",
        "desc": "개헌저지선(100석)만 간신히 방어한 사상 최악의 집권 여당 성적표. 한덕수 총리 및 참모진 총사퇴."
      },
      {
        "tag": "인사 악재",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "이종섭 호주대사 도피성 출국 논란 & 황상무 회칼 테러 발언",
        "desc": "총선 직전 핵심 악재들이 겹치며 수도권 부동층과 중도 민심의 치명적 이탈 야기."
      },
      {
        "tag": "민심 이반",
        "tagBg": "rgba(191, 90, 242, 0.15)",
        "tagColor": "#BF5AF2",
        "title": "'대파 875원' 논란과 고물가 심판론의 쓰나미",
        "desc": "서민 밥상물가 폭등에 대한 체감 불만이 투표장 분노로 폭발, 조국혁신당 비례 12석 돌풍 견인."
      }
    ],
    "partySupport": "국민의힘 30~32% vs 더불어민주당 37~39% (조국혁신당 12%)",
    "analysis": "한국갤럽 23%로 취임 후 최저치 추락. 국정 운영 기조 전면 전환 요구가 빗발쳤으며, 22대 국회 개원과 함께 여소야대 의회 권력에 포위된 식물정부 위기 직면."
  },
  {
    "idx": 12,
    "date": "2024.06 (동해 영일만 대왕고래 발표)",
    "shortLabel": "24.06 대왕고래",
    "period": "집권 3년차 전반기 자원 외교 승부수",
    "approval": {
      "nbs": [
        29,
        63
      ],
      "gallup": [
        26,
        66
      ],
      "realm": [
        30.1,
        65.1
      ],
      "mbc": [
        28.5,
        64.8
      ],
      "avgPos": 28.4,
      "avgNeg": 64.8
    },
    "videoId": "k3Q8zBVLlls",
    "videoTitle": "동해 심해 가스전 '대왕고래' 최대 140억 배럴 석유·가스전 탐사시추 발표",
    "events": [
      {
        "tag": "자원 개발",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "대통령 첫 국정브리핑으로 동해 심해 가스전 시추 발표",
        "desc": "포항 영일만 앞바다 최대 140억 배럴 규모 석유·가스 매장 가능성 직접 발표."
      },
      {
        "tag": "검증 논란",
        "tagBg": "rgba(255, 159, 10, 0.15)",
        "tagColor": "#FF9F0A",
        "title": "미국 액트지오(Act-Geo)사 신뢰성 및 세금 낭비 공방",
        "desc": "본사 주소지 논란과 아브레우 고문 방한 기자회견 속 야당의 국정전환용 쇼 공세 격돌."
      },
      {
        "tag": "국회 대치",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "22대 국회 원 구성 단독 강행 및 상임위 전면 보이콧",
        "desc": "야당의 법사위·운영위 독식 속 여야 원내 대치 극대화."
      }
    ],
    "partySupport": "국민의힘 30~32% vs 더불어민주당 35~37%",
    "analysis": "대형 자원 호재 발표에도 불구하고 총선 패배 후유증과 야당의 철저한 검증 공세로 지지율 반등 모멘텀 창출 실패. 20%대 후반 박스권 정체 지속."
  },
  {
    "idx": 13,
    "date": "2024.09 (체코 두코바니 원전 24조 수주)",
    "shortLabel": "24.09 체코원전",
    "period": "K-원전 르네상스와 글로벌 세일즈 외교",
    "approval": {
      "nbs": [
        27,
        63
      ],
      "gallup": [
        23,
        67
      ],
      "realm": [
        30.3,
        66.1
      ],
      "mbc": [
        26.8,
        65.4
      ],
      "avgPos": 26.8,
      "avgNeg": 65.4
    },
    "videoId": "gtV_vBB6lPw",
    "videoTitle": "총 24조 원 규모 체코 두코바니 신규 원전 건설 사업 우선협상대상자 선정",
    "events": [
      {
        "tag": "원전 수출",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "체코 신규 원전 2기 24조 원 우선협상대상자 선정",
        "desc": "2009년 UAE 바라카 원전 이후 15년 만의 쾌거. '팀 코리아' K-원전의 유럽 본토 교두보 확보."
      },
      {
        "tag": "외교 방문",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "체코 공식 방문 및 한-체코 원전 전주기 협력 MOU 체결",
        "desc": "파벨 대통령과의 회담을 통해 고속철도·우주항공·배터리까지 포괄적 산업 협력 확대."
      },
      {
        "tag": "수익성 공방",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "웨스팅하우스 지재권 분쟁 및 덤핑 수주 의혹 정쟁",
        "desc": "야당의 금융지원 퍼주기 비판과 여당의 원전 생태계 부활 자축이 팽팽히 맞섬."
      }
    ],
    "partySupport": "국민의힘 31~33% vs 더불어민주당 36~38%",
    "analysis": "역대급 산업 수출 낭보에도 불구하고 국내 정치의 '김건희 여사 공천 개입 의혹'과 '응급실 뺑뺑이 의료 대란' 이슈에 가려지며 지지율 반등이 제약됨."
  },
  {
    "idx": 14,
    "date": "2024.10 (명태균 녹취록 파문 & 지지율 19%)",
    "shortLabel": "24.10 명태균녹취",
    "period": "보수 텃밭 균열과 임기 반환점 위기",
    "approval": {
      "nbs": [
        24,
        67
      ],
      "gallup": [
        19,
        72
      ],
      "realm": [
        24.6,
        71.4
      ],
      "mbc": [
        22.8,
        70.1
      ],
      "avgPos": 22.8,
      "avgNeg": 70.1
    },
    "videoId": "Oiz8KUZ8Dxk",
    "videoTitle": "명태균 통화 녹취록 공개 및 한국갤럽 국정 지지율 19% 최저치 기록",
    "events": [
      {
        "tag": "녹취 폭로",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "민주당, 윤 대통령-명태균 육성 통화 녹취록 공개",
        "desc": "‘김영선이 좀 해줘라 그랬는데’ 육성이 공개되며 취임 전 공천 개입 의혹이 일파만파 확산."
      },
      {
        "tag": "지지율 붕괴",
        "tagBg": "rgba(255, 59, 48, 0.15)",
        "tagColor": "#FF3B30",
        "title": "한국갤럽 기준 국정 지지율 19% 사상 최저치 기록",
        "desc": "보수 텃밭 대구·경북(TK)에서도 긍정 18% vs 부정 69%로 붕괴되며 정권 출범 이래 최대 위기."
      },
      {
        "tag": "쇄신 대국민담화",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "대통령 대국민 담화 및 고개 숙인 사과",
        "desc": "대외활동 중단, 특별감찰관 수용 기조 천명 및 인적 쇄신 개편 착수."
      }
    ],
    "partySupport": "국민의힘 28~30% vs 더불어민주당 38~40%",
    "analysis": "임기 반환점을 앞두고 심리적 마지노선인 20%선이 무너짐. 전통적 콘크리트 지지층인 70대 이상과 TK 지역마저 등을 돌리며 헌정사상 유례없는 조기 레임덕 국면 전개."
  },
  {
    "idx": 15,
    "date": "2026.10 (현재 / 후반기 4대 개혁 완수)",
    "shortLabel": "26.10 현재",
    "period": "집권 후반기 4대 개혁 완수 및 차기 지형 형성기",
    "approval": {
      "nbs": [
        28,
        64
      ],
      "gallup": [
        22,
        69
      ],
      "realm": [
        24.6,
        71.4
      ],
      "mbc": [
        24.8,
        68.2
      ],
      "avgPos": 24.8,
      "avgNeg": 68.2
    },
    "videoId": "pFgZ6za8yBA",
    "videoTitle": "윤석열 대통령, 국회에 연금·의료·교육·노동 4대 개혁 완수 협력 촉구",
    "events": [
      {
        "tag": "국정 개혁",
        "tagBg": "rgba(48, 209, 88, 0.15)",
        "tagColor": "#30D158",
        "title": "연금·의료·교육·노동 4대 개혁 후반기 완수 드라이브",
        "desc": "국민연금 모수개혁 정부안 국회 논의 촉구 및 의정 갈등 출구 전략 모색."
      },
      {
        "tag": "사법 격돌",
        "tagBg": "rgba(255, 69, 58, 0.15)",
        "tagColor": "#FF453A",
        "title": "조희대 대법아카이브 국정조사 요구서 제출 및 특검 충돌",
        "desc": "선관위 특검의 투표지 반출 등 선거 사법 쟁점화 속 여야의 전방위 정면 대치 지속."
      },
      {
        "tag": "정치 판세",
        "tagBg": "rgba(0, 113, 227, 0.15)",
        "tagColor": "#2997FF",
        "title": "2026 지방선거 및 차기 대선 구도 조기 태동",
        "desc": "오세훈 무죄 후 여권 '장동혁·한동훈·오세훈' 3각 축 형성 vs 야권 이재명 중심 진영 결집."
      }
    ],
    "partySupport": "국민의힘 25~28% vs 더불어민주당 36~38%",
    "analysis": "NBS 28%(+2%p), 갤럽 22%, 리얼미터 24.6%, 여론M 24.8%로 20%대 중반 횡보세. 부정 평가는 64~71% 수준으로 견고함. 후반기 개혁 과제 추진과 사법 공방 속에서 양대 진영 간 콘크리트 결집 양상이 뚜렷하게 전개됨."
  }
];

    window.FOUR_POLLS_HISTORY = window.INFLECTION_EVENTS_DATA.map(d => ({
      date: d.date,
      nbs: d.approval.nbs,
      gallup: d.approval.gallup,
      realm: d.approval.realm,
      mbc: d.approval.mbc
    }));

    window.HISTORICAL_PRESIDENT_DATA = [
      { name: "문재인", color: "#3B82F6", pts: [81, 52, 47, 45, 42] },
      { name: "박근혜", color: "#EF4444", pts: [54, 42, 34, 29, 12] },
      { name: "이명박", color: "#10B981", pts: [52, 27, 44, 33, 24] },
      { name: "노무현", color: "#F59E0B", pts: [60, 25, 27, 23, 24] },
      { name: "현 정권", color: "#2997FF", width: 3.5, pts: [52, 31.7, 27.2, 23.8, 24.8] }
    ];

    window.currentPollViewMode = 'all';
    window.currentInflectionIdx = 4;
    window.isPollTrajectoryPlaying = false;

    // 뷰 모드 전환 함수
    window.setPollViewMode = function(mode) {
      window.currentPollViewMode = mode;
      
      const pills = [
        { id: 'btnPollModeAll', mode: 'all' },
        { id: 'btnPollModeSpread', mode: 'spread' },
        { id: 'btnPollModeHistorical', mode: 'historical' },
        { id: 'btnPollModeEvents', mode: 'events' }
      ];

      pills.forEach(p => {
        const btn = document.getElementById(p.id);
        if (btn) btn.classList.toggle('active', p.mode === mode);
      });

      const titleEl = document.getElementById('pollGraphTitle');
      const badgeEl = document.getElementById('pollGraphBadge');

      if (mode === 'all') {
        if (badgeEl) badgeEl.innerText = '📈 시계열 동적 4대 조사 궤적';
        if (titleEl) titleEl.innerText = '현 정권 4대 조사 직무수행 평가 지지율 궤적 (2022.05 취임 ~ 2026.10 현재)';
      } else if (mode === 'spread') {
        if (badgeEl) badgeEl.innerText = '⚡ 긍정 vs 부정 격차 분석';
        if (titleEl) titleEl.innerText = '대통령 직무수행 긍정(24.8%) vs 부정(68.2%) 데드크로스 및 격차(-43.4%p) 궤적';
      } else if (mode === 'historical') {
        if (badgeEl) badgeEl.innerText = '🏛️ 역대 5대 정권 동 시기 비교';
        if (titleEl) titleEl.innerText = '역대 대통령 취임~집권 후반기(5개 분기점) 지지율 비교 궤적 (문재인·박근혜·이명박·노무현 vs 현 정권)';
      } else if (mode === 'events') {
        if (badgeEl) badgeEl.innerText = '🔍 5대 변곡점 핵심 사건 연동 뷰';
        if (titleEl) titleEl.innerText = '정권 지지율 급락·반등 5대 변곡점 및 결정적 정치사건 타임라인 연동';
      }

      window.renderFourPollsChart(window.currentInflectionIdx, mode);
    };

    // 변곡점 선택 함수
    window.setPresidentTermPoint = function(idx) {
      window.currentInflectionIdx = idx;
      window.renderFourPollsChart(idx, window.currentPollViewMode);

      document.querySelectorAll('.poll-time-pill').forEach((btn, i) => {
        btn.classList.toggle('active', i === idx);
        if (i === idx) {
          btn.style.background = '#2997FF';
          btn.style.color = '#FFF';
          btn.style.fontWeight = '700';
          btn.style.border = 'none';
        } else {
          btn.style.background = 'rgba(255,255,255,0.06)';
          btn.style.color = '#94A3B8';
          btn.style.fontWeight = 'normal';
          btn.style.border = '1px solid rgba(255,255,255,0.12)';
        }
      });

      // 4대 조사 하단 카드 업데이트
      const data = window.FOUR_POLLS_HISTORY[idx];
      const grid = document.getElementById('fourPollsGridContainer');
      if (grid && grid.children.length >= 4) {
        updatePollCardVal(grid.children[0], "NBS 전국지표조사", data.nbs[0], data.nbs[1]);
        updatePollCardVal(grid.children[1], "한국갤럽 (Gallup)", data.gallup[0], data.gallup[1]);
        updatePollCardVal(grid.children[2], "리얼미터 (Realmeter)", data.realm[0], data.realm[1]);
        updatePollCardVal(grid.children[3], "MBC 여론M (메타)", data.mbc[0], data.mbc[1]);
      }

      // 하단 변곡점 브리프 카드 업데이트
      window.updateInflectionBriefCard(idx);
    };

    function updatePollCardVal(card, title, pos, neg) {
      if (!card) return;
      const divs = card.querySelectorAll('div');
      divs.forEach(d => {
        if (d.style.fontSize && d.style.fontSize.includes('1.85rem')) {
          if (d.style.color && d.style.color.includes('2997FF')) {
            d.innerHTML = `${pos}<span style="font-size: 1rem; font-weight: 700;">%</span>`;
          } else if (d.style.color && d.style.color.includes('FF453A')) {
            d.innerHTML = `${neg}<span style="font-size: 1rem; font-weight: 700;">%</span>`;
          }
        }
      });
      const ratioBars = card.querySelectorAll('div[style*="height: 6px"] > div');
      if (ratioBars.length >= 3) {
        ratioBars[0].style.width = `${pos}%`;
        ratioBars[2].style.width = `${neg}%`;
        const mid = 100 - pos - neg;
        ratioBars[1].style.width = `${mid > 0 ? mid : 0}%`;
      }
    }

    // 하단 변곡점 사건 실시간 브리프 카드 동기화
    window.updateInflectionBriefCard = function(idx) {
      const card = document.getElementById('inflectionBriefCard');
      if (!card) return;

      const data = window.INFLECTION_EVENTS_DATA[idx];
      if (!data) return;

      let eventsHtml = '';
      data.events.forEach(ev => {
        eventsHtml += `
          <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 10px 14px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
              <span class="inflection-event-tag" style="background: ${ev.tagBg}; color: ${ev.tagColor};">${ev.tag}</span>
              <strong style="font-size: 0.85rem; color: #F5F5F7;">${ev.title}</strong>
            </div>
            <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.45;">${ev.desc}</div>
          </div>
        `;
      });

      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 0.78rem; font-weight: 800; color: #2997FF; background: rgba(0, 113, 227, 0.15); padding: 2px 8px; border-radius: 4px;">📌 선택 변곡점 팩트 브리프</span>
            <strong style="font-size: 1.05rem; color: #FFFFFF;">${data.date}</strong>
            <span style="font-size: 0.82rem; color: #2997FF; font-weight: 700;">평균 긍정 ${data.approval.avgPos}% / 부정 ${data.approval.avgNeg}%</span>
          </div>
          <button onclick="openInflectionModal(${idx})" style="background: #2997FF; color: #FFF; border: none; padding: 4px 14px; border-radius: 6px; font-size: 0.78rem; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
            🔍 변곡점 심층 팩트체크 팝업 열기 ↗
          </button>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 10px;">
          ${eventsHtml}
        </div>

        <div style="font-size: 0.8rem; color: #D1D5DB; line-height: 1.5; background: rgba(0,0,0,0.25); padding: 8px 12px; border-radius: 6px; border-left: 3px solid #2997FF;">
          <strong>💡 싱크탱크 분석 요약:</strong> ${data.analysis}
        </div>
      `;
    };

    // 팝업 모달 열기 / 닫기
    window.openInflectionModal = function(idx) {
      window.currentInflectionIdx = idx;
      const modal = document.getElementById('inflectionEventModal');
      if (!modal) return;

      const data = window.INFLECTION_EVENTS_DATA[idx];
      if (!data) return;

      const badge = document.getElementById('modalInflectionBadge');
      if (badge) badge.innerText = `변곡점 ${idx + 1} / ${window.INFLECTION_EVENTS_DATA.length}`;
      
      const title = document.getElementById('modalInflectionTitle');
      if (title) title.innerText = data.date;
      
      const period = document.getElementById('modalInflectionPeriod');
      if (period) period.innerText = data.period;

      // Video iframe update
      const videoIframe = document.getElementById('modalInflectionVideoIframe');
      if (videoIframe) {
        if (data.videoId) {
          videoIframe.src = 'https://www.youtube.com/embed/' + data.videoId + '?autoplay=1&enablejsapi=1';
        } else {
          videoIframe.src = '';
        }
      }

      const statsGrid = document.getElementById('modalPollStatsGrid');
      if (statsGrid) {
        statsGrid.innerHTML = `
          <div style="background: rgba(0, 113, 227, 0.1); padding: 10px; border-radius: 8px; text-align: center;">
            <div style="font-size: 0.72rem; color: #2997FF; font-weight: 700;">NBS 지표조사</div>
            <div style="font-size: 1.1rem; font-weight: 800; color: #FFF;">${data.approval.nbs[0]}%</div>
            <div style="font-size: 0.68rem; color: #FF453A;">부정 ${data.approval.nbs[1]}%</div>
          </div>
          <div style="background: rgba(100, 210, 255, 0.1); padding: 10px; border-radius: 8px; text-align: center;">
            <div style="font-size: 0.72rem; color: #64D2FF; font-weight: 700;">한국갤럽</div>
            <div style="font-size: 1.1rem; font-weight: 800; color: #FFF;">${data.approval.gallup[0]}%</div>
            <div style="font-size: 0.68rem; color: #FF453A;">부정 ${data.approval.gallup[1]}%</div>
          </div>
          <div style="background: rgba(191, 90, 242, 0.1); padding: 10px; border-radius: 8px; text-align: center;">
            <div style="font-size: 0.72rem; color: #BF5AF2; font-weight: 700;">리얼미터</div>
            <div style="font-size: 1.1rem; font-weight: 800; color: #FFF;">${data.approval.realm[0]}%</div>
            <div style="font-size: 0.68rem; color: #FF453A;">부정 ${data.approval.realm[1]}%</div>
          </div>
          <div style="background: rgba(255, 159, 10, 0.1); padding: 10px; border-radius: 8px; text-align: center;">
            <div style="font-size: 0.72rem; color: #FF9F0A; font-weight: 700;">여론M 메타</div>
            <div style="font-size: 1.1rem; font-weight: 800; color: #FFF;">${data.approval.mbc[0]}%</div>
            <div style="font-size: 0.68rem; color: #FF453A;">부정 ${data.approval.mbc[1]}%</div>
          </div>
        `;
      }

      const eventsList = document.getElementById('modalEventsList');
      if (eventsList) {
        let eventsHtml = '';
        data.events.forEach(ev => {
          eventsHtml += `
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 14px;">
              <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                <span style="background: ${ev.tagBg}; color: ${ev.tagColor}; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">${ev.tag}</span>
                <span style="font-size: 0.95rem; font-weight: 800; color: #FFF;">${ev.title}</span>
              </div>
              <p style="font-size: 0.84rem; color: #94A3B8; margin: 0; line-height: 1.5;">${ev.desc}</p>
            </div>
          `;
        });
        eventsList.innerHTML = eventsHtml;
      }

      const partyEl = document.getElementById('modalPartySupport');
      if (partyEl) partyEl.innerText = data.partySupport;

      const analysisEl = document.getElementById('modalThinkTankAnalysis');
      if (analysisEl) analysisEl.innerText = data.analysis;

      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    };

    window.closeInflectionModal = function() {
      const modal = document.getElementById('inflectionEventModal');
      if (modal) modal.style.display = 'none';
      const videoIframe = document.getElementById('modalInflectionVideoIframe');
      if (videoIframe) videoIframe.src = '';
      document.body.style.overflow = '';
    };

    window.changeInflectionModal = function(step) {
      let nextIdx = window.currentInflectionIdx + step;
      if (nextIdx < 0) nextIdx = 0;
      if (nextIdx > 4) nextIdx = 4;
      window.setPresidentTermPoint(nextIdx);
      window.openInflectionModal(nextIdx);
    };

    // 정권 초기~현재 궤적 애니메이션 재생
    window.playPresidentTrajectory = function() {
      if (window.isPollTrajectoryPlaying) return;
      window.isPollTrajectoryPlaying = true;
      const btn = document.getElementById('btnPlayTrajectory');
      if (btn) btn.innerHTML = '⏳ 궤적 재생 중...';

      let step = 0;
      window.setPresidentTermPoint(0);

      const interval = setInterval(() => {
        step++;
        if (step <= 4) {
          window.setPresidentTermPoint(step);
        } else {
          clearInterval(interval);
          window.isPollTrajectoryPlaying = false;
          if (btn) btn.innerHTML = '▶️ 정권 초기~현재 궤적 애니메이션 재생';
        }
      }, 900);
    };

    // =========================================================================
    // 📈 핵심 SVG 동적 렌더링 엔진 (4대 모드 지원)
    // =========================================================================
    window.renderFourPollsChart = function(activeIdx = 4, mode = window.currentPollViewMode || 'all') {
      const container = document.getElementById('fourPollsInteractiveSvgContainer');
      const legendContainer = document.getElementById('fourPollsLegendContainer');
      if (!container) return;

      const w = 1140;
      const h = 260;
      const padL = 60;
      const padR = 60;
      const padT = 30;
      const padB = 45;
      const plotW = w - padL - padR;
      const plotH = h - padT - padB;

      const dates = window.INFLECTION_EVENTS_DATA.map(d => d.shortLabel);
      const getX = i => padL + (i / (dates.length - 1)) * plotW;

      // Update Legend depending on mode
      if (legendContainer) {
        if (mode === 'all') {
          legendContainer.innerHTML = `
            <span style="color: #2997FF; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 10px; border-radius: 50%; background: #2997FF; display: inline-block;"></span> NBS (28%)</span>
            <span style="color: #64D2FF; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 10px; border-radius: 50%; background: #64D2FF; display: inline-block;"></span> 갤럽 (22%)</span>
            <span style="color: #BF5AF2; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 10px; border-radius: 50%; background: #BF5AF2; display: inline-block;"></span> 리얼미터 (24.6%)</span>
            <span style="color: #FF9F0A; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 10px; border-radius: 50%; background: #FF9F0A; display: inline-block;"></span> 여론M (24.8%)</span>
          `;
        } else if (mode === 'spread') {
          legendContainer.innerHTML = `
            <span style="color: #30D158; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 10px; border-radius: 50%; background: #30D158; display: inline-block;"></span> 평균 긍정 평가 (24.8%)</span>
            <span style="color: #FF453A; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 10px; border-radius: 50%; background: #FF453A; display: inline-block;"></span> 평균 부정 평가 (68.2%)</span>
            <span style="color: #FF9F0A; display: inline-flex; align-items: center; gap: 4px;">⚡ 격차: -43.4%p (데드크로스 고착)</span>
          `;
        } else if (mode === 'historical') {
          legendContainer.innerHTML = `
            <span style="color: #2997FF; display: inline-flex; align-items: center; gap: 4px; font-weight: 900;"><span style="width: 12px; height: 4px; background: #2997FF; display: inline-block;"></span> 현 정권 (24.8%)</span>
            <span style="color: #3B82F6; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 2px; background: #3B82F6; display: inline-block;"></span> 문재인 (45%)</span>
            <span style="color: #EF4444; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 2px; background: #EF4444; display: inline-block;"></span> 박근혜 (29%)</span>
            <span style="color: #10B981; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 2px; background: #10B981; display: inline-block;"></span> 이명박 (33%)</span>
            <span style="color: #F59E0B; display: inline-flex; align-items: center; gap: 4px;"><span style="width: 10px; height: 2px; background: #F59E0B; display: inline-block;"></span> 노무현 (23%)</span>
          `;
        } else if (mode === 'events') {
          legendContainer.innerHTML = `
            <span style="color: #2997FF; display: inline-flex; align-items: center; gap: 4px;">💡 변곡점 클릭 시 사건 상세 팝업 오픈</span>
          `;
        }
      }

      let minVal = 15;
      let maxVal = 75;
      if (mode === 'historical') { minVal = 10; maxVal = 85; }
      else if (mode === 'spread') { minVal = 15; maxVal = 75; }

      const getY = val => padT + (1 - (val - minVal) / (maxVal - minVal)) * plotH;

      let svg = `<svg viewBox="0 0 ${w} ${h}" style="width:100%; height:100%; overflow:visible;" xmlns="http://www.w3.org/2000/svg">`;

      // Defs: Gradients and Markers
      svg += `
        <defs>
          <linearGradient id="spreadAreaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#FF453A" stop-opacity="0.25" />
            <stop offset="100%" stop-color="#30D158" stop-opacity="0.05" />
          </linearGradient>
          <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>
      `;

      // Y-axis grid lines
      const yTicks = (mode === 'historical') ? [20, 35, 50, 65, 80] : [20, 30, 40, 50, 60, 70];
      yTicks.forEach(val => {
        const y = getY(val);
        svg += `
          <line x1="${padL}" y1="${y}" x2="${w - padR}" y2="${y}" stroke="rgba(255, 255, 255, 0.08)" stroke-dasharray="3,3" />
          <text x="${padL - 12}" y="${y + 4}" fill="#86868B" font-size="11" text-anchor="end" font-weight="600">${val}%</text>
        `;
      });

      // X-axis milestone labels & vertical reference guides
      dates.forEach((d, i) => {
        const x = getX(i);
        const isActive = (i === activeIdx);
        const color = isActive ? '#2997FF' : '#86868B';
        const weight = isActive ? '800' : '600';
        svg += `
          <line x1="${x}" y1="${padT}" x2="${x}" y2="${h - padB}" stroke="${isActive ? 'rgba(41, 151, 255, 0.35)' : 'rgba(255, 255, 255, 0.04)'}" stroke-dasharray="${isActive ? 'none' : '2,2'}" stroke-width="${isActive ? 2 : 1}" />
          <text x="${x}" y="${h - 14}" fill="${color}" font-size="11.5" text-anchor="middle" font-weight="${weight}" style="cursor: pointer;" onclick="setPresidentTermPoint(${i}); openInflectionModal(${i});">${d}</text>
        `;
      });

      // Active Vertical Scrubber Line & Pulsing Ring
      const activeX = getX(activeIdx);
      svg += `
        <line x1="${activeX}" y1="${padT - 6}" x2="${activeX}" y2="${h - padB}" stroke="#2997FF" stroke-width="2.5" stroke-dasharray="4,3" />
        <circle cx="${activeX}" cy="${padT - 6}" r="5" fill="#2997FF" />
        <circle cx="${activeX}" cy="${padT - 6}" r="12" fill="none" stroke="#2997FF" class="poll-pulse-ring" />
      `;

      // Helper function to draw curved paths
      const makeCurvedPath = pts => {
        let pathD = '';
        pts.forEach((pt, idx) => {
          if (idx === 0) pathD += `M ${pt.x} ${pt.y}`;
          else {
            const prev = pts[idx - 1];
            const cpX = (prev.x + pt.x) / 2;
            pathD += ` C ${cpX} ${prev.y}, ${cpX} ${pt.y}, ${pt.x} ${pt.y}`;
          }
        });
        return pathD;
      };

      // -----------------------------------------------------------------------
      // MODE 1: ALL 4 AGENCIES COMPARISON (4대 조사 종합 궤적)
      // -----------------------------------------------------------------------
      if (mode === 'all' || mode === 'events') {
        const series = [
          { key: 'nbs', label: 'NBS', color: '#2997FF', width: 3.5 },
          { key: 'gallup', label: '갤럽', color: '#64D2FF', width: 2.5 },
          { key: 'realm', label: '리얼미터', color: '#BF5AF2', width: 2.5 },
          { key: 'mbc', label: '여론M', color: '#FF9F0A', width: 2.5 }
        ];

        series.forEach(s => {
          let pts = window.FOUR_POLLS_HISTORY.map((d, i) => ({ x: getX(i), y: getY(d[s.key][0]), val: d[s.key][0] }));
          let pathD = makeCurvedPath(pts);

          svg += `<path d="${pathD}" fill="none" stroke="${s.color}" stroke-width="${s.width}" stroke-linecap="round" stroke-linejoin="round" class="animated-poll-path" opacity="0.9" />`;

          // Points
          pts.forEach((pt, idx) => {
            const isActive = (idx === activeIdx);
            const r = isActive ? 7 : 4;
            svg += `
              <circle cx="${pt.x}" cy="${pt.y}" r="${r}" fill="#10141E" stroke="${s.color}" stroke-width="${isActive ? 3.5 : 2}" style="cursor: pointer;" onclick="setPresidentTermPoint(${idx}); openInflectionModal(${idx});" />
            `;
            
            if (isActive) {
              svg += `
                <rect x="${pt.x - 22}" y="${pt.y - 25}" width="44" height="18" rx="4" fill="#10141E" stroke="${s.color}" stroke-width="1.5" />
                <text x="${pt.x}" y="${pt.y - 12}" fill="#FFFFFF" font-size="10.5" font-weight="800" text-anchor="middle">${pt.val}%</text>
              `;
            }
          });
        });

        // Event callout flags in 'events' mode
        if (mode === 'events') {
          window.INFLECTION_EVENTS_DATA.forEach((d, i) => {
            const x = getX(i);
            const y = getY(d.approval.avgPos);
            svg += `
              <g style="cursor: pointer;" onclick="openInflectionModal(${i})">
                <rect x="${x - 55}" y="${padT + 10 + (i % 2) * 35}" width="110" height="24" rx="6" fill="#1A1F2C" stroke="#2997FF" stroke-width="1" />
                <text x="${x}" y="${padT + 26 + (i % 2) * 35}" fill="#FFF" font-size="10" font-weight="700" text-anchor="middle">📌 ${d.events[0].tag}</text>
              </g>
            `;
          });
        }
      }

      // -----------------------------------------------------------------------
      // MODE 2: SPREAD (긍정 vs 부정 평가 격차 & 데드크로스)
      // -----------------------------------------------------------------------
      else if (mode === 'spread') {
        let posPts = window.INFLECTION_EVENTS_DATA.map((d, i) => ({ x: getX(i), y: getY(d.approval.avgPos), val: d.approval.avgPos }));
        let negPts = window.INFLECTION_EVENTS_DATA.map((d, i) => ({ x: getX(i), y: getY(d.approval.avgNeg), val: d.approval.avgNeg }));

        // Shaded Gap Area
        let areaD = makeCurvedPath(posPts);
        for (let i = negPts.length - 1; i >= 0; i--) {
          areaD += ` L ${negPts[i].x} ${negPts[i].y}`;
        }
        areaD += ' Z';
        svg += `<path d="${areaD}" fill="url(#spreadAreaGrad)" />`;

        // Draw Pos & Neg Lines
        svg += `<path d="${makeCurvedPath(posPts)}" fill="none" stroke="#30D158" stroke-width="3.5" class="animated-poll-path" />`;
        svg += `<path d="${makeCurvedPath(negPts)}" fill="none" stroke="#FF453A" stroke-width="3.5" class="animated-poll-path" />`;

        // Points
        posPts.forEach((pt, idx) => {
          const isActive = (idx === activeIdx);
          svg += `<circle cx="${pt.x}" cy="${pt.y}" r="${isActive ? 7 : 4}" fill="#10141E" stroke="#30D158" stroke-width="2.5" style="cursor:pointer;" onclick="setPresidentTermPoint(${idx}); openInflectionModal(${idx});" />`;
          if (isActive) {
            svg += `<text x="${pt.x}" y="${pt.y - 12}" fill="#30D158" font-size="11" font-weight="800" text-anchor="middle">긍정 ${pt.val}%</text>`;
          }
        });
        negPts.forEach((pt, idx) => {
          const isActive = (idx === activeIdx);
          svg += `<circle cx="${pt.x}" cy="${pt.y}" r="${isActive ? 7 : 4}" fill="#10141E" stroke="#FF453A" stroke-width="2.5" style="cursor:pointer;" onclick="setPresidentTermPoint(${idx}); openInflectionModal(${idx});" />`;
          if (isActive) {
            svg += `<text x="${pt.x}" y="${pt.y - 12}" fill="#FF453A" font-size="11" font-weight="800" text-anchor="middle">부정 ${pt.val}%</text>`;
          }
        });

        // Dead Cross Marker (approx between index 0 and 1, around 2022.07)
        const dcX = getX(0) + (getX(1) - getX(0)) * 0.45;
        const dcY = getY(44);
        svg += `
          <g>
            <circle cx="${dcX}" cy="${dcY}" r="6" fill="#FF453A" stroke="#FFF" stroke-width="2" />
            <rect x="${dcX - 45}" y="${dcY - 32}" width="90" height="20" rx="4" fill="#FF453A" />
            <text x="${dcX}" y="${dcY - 18}" fill="#FFF" font-size="10" font-weight="800" text-anchor="middle">⚡ 데드크로스 (22.07)</text>
          </g>
        `;
      }

      // -----------------------------------------------------------------------
      // MODE 3: HISTORICAL PRESIDENTS COMPARISON (역대 정권 동 시기 비교)
      // -----------------------------------------------------------------------
      else if (mode === 'historical') {
        window.HISTORICAL_PRESIDENT_DATA.forEach(p => {
          let pts = p.pts.map((val, i) => ({ x: getX(i), y: getY(val), val }));
          let pathD = makeCurvedPath(pts);
          const isCurrent = (p.name === "현 정권");

          svg += `
            <path d="${pathD}" fill="none" stroke="${p.color}" stroke-width="${isCurrent ? 4 : 1.8}" stroke-dasharray="${isCurrent ? 'none' : '4,3'}" class="animated-poll-path" opacity="${isCurrent ? 1 : 0.6}" />
          `;

          // Label at end of line
          const lastPt = pts[pts.length - 1];
          svg += `
            <text x="${lastPt.x + 8}" y="${lastPt.y + 4}" fill="${p.color}" font-size="11" font-weight="${isCurrent ? '800' : '600'}">${p.name} (${lastPt.val}%)</text>
          `;

          if (isCurrent) {
            pts.forEach((pt, idx) => {
              const isActive = (idx === activeIdx);
              svg += `<circle cx="${pt.x}" cy="${pt.y}" r="${isActive ? 7 : 4}" fill="#10141E" stroke="${p.color}" stroke-width="3" style="cursor:pointer;" onclick="setPresidentTermPoint(${idx}); openInflectionModal(${idx});" />`;
              if (isActive) {
                svg += `
                  <rect x="${pt.x - 24}" y="${pt.y - 25}" width="48" height="18" rx="4" fill="#10141E" stroke="${p.color}" stroke-width="1.5" />
                  <text x="${pt.x}" y="${pt.y - 12}" fill="#FFFFFF" font-size="11" font-weight="800" text-anchor="middle">${pt.val}%</text>
                `;
              }
            });
          }
        });
      }

      svg += `</svg>`;
      container.innerHTML = svg;
    };

    // =========================================================================
    // 🎨 역대 만평 아카이브 실시간 전환 로더
    // =========================================================================
    window.loadArchiveCartoon = function(dateStr) {
      const img = document.getElementById('currentCartoonImg');
      const webp = document.getElementById('currentCartoonWebp');
      const title = document.getElementById('cartoonMainTitle');
      const points = document.getElementById('cartoonMainPoints');
      const dateEl = document.getElementById('cartoonFactDate');
      const downloadBtn = document.getElementById('cartoonDownloadBtn');
      const factGrid = document.getElementById('cartoonFactGrid');

      // Update active button styles
      ['20261110', '20261031', '20261030', '20261029', '20261028'].forEach(d => {
        const btn = document.getElementById('btnCartoon' + d);
        if (btn) {
          if (d === dateStr) {
            btn.style.background = 'rgba(16, 185, 129, 0.2)';
            btn.style.border = '1px solid #10B981';
            btn.style.color = '#10B981';
            btn.style.fontWeight = '700';
          } else {
            btn.style.background = 'rgba(255, 255, 255, 0.06)';
            btn.style.border = '1px solid rgba(255, 255, 255, 0.12)';
            btn.style.color = '#86868B';
            btn.style.fontWeight = 'normal';
          }
        }
      });

      if (dateStr === '20261110') {
        if (img) img.src = window.__CARTOON_20261110_URI;
        if (webp) webp.srcset = window.__CARTOON_20261110_URI;
        if (downloadBtn) {
          downloadBtn.href = window.__CARTOON_20261110_URI;
          downloadBtn.download = 'RYUYOUNGSUN_Editorial_Cartoon_20261110.webp';
        }
        if (dateEl) dateEl.innerText = '2026.11.10 화요일 정밀 팩트 확정치 반영';
        if (title) title.innerText = '『"금값 4,100달러에도 사재기는 멈추지 않는다!" 중앙은행들의 탈달러 금 러시와 홀로 잠든 한국의 금고』';
        if (points) {
          points.innerHTML = `
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">①</span>
              <div><strong>9월 61톤 폭풍 매수와 폴란드의 기습:</strong> 7월 23톤, 8월 39톤에서 9월 61톤으로 가속된 글로벌 중앙은행의 금 순매수는 올해 월간 최대치입니다(WGC·IMF 2026년 9월 데이터). 보유량 11위 폴란드가 9월 한 달 25톤, 1~9월 누적 123톤을 사들이며 올해 최대 매수국에 올랐습니다(9월 중국은 23톤).</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">②</span>
              <div><strong>달러 무기화의 역설, 5,000톤 시대:</strong> 러시아 준비자산 동결 이후 "동결 불가능한 준비자산"으로 금이 재평가되고 있습니다. 2025년 연간 금 수요는 사상 처음 5,000톤을 넘었고 가격은 53차례 신기록을 썼습니다(WGC). 11월 9일 현재 온스당 4,120달러로 2주 만에 최고치, 1월 29일엔 사상 최고 5,595달러를 기록했습니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">③</span>
              <div><strong>12년째 잠든 한국의 금고:</strong> 미국 8,134톤, 독일 3,349톤, 중국 2,410톤의 금고 전쟁 속 한국은행의 실물 금 보유는 104.4톤으로 외환보유액의 1.1%(6월 말 기준)에 그칩니다. 2013년 이후 실물 추가 매입은 없었으나 최근 소규모 금 ETF 매입과 12월 국산 금 매입 검토가 보도되며, 대전환기 자산 리밸런싱 논의가 시작됐다는 것이 이 만평의 경고입니다.</div>
            </div>
          `;
        }
        if (factGrid) {
          factGrid.innerHTML = `
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">9월 중앙은행 순매수</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #F59E0B;">61톤</div>
              <div style="font-size: 0.68rem; color: #F59E0B;">올해 월간 최대 · 7월 23t→8월 39t</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">국제 금값(11/9 기준)</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FFD60A;">$4,120</div>
              <div style="font-size: 0.68rem; color: #FFD60A;">2주 만에 최고치 · 1/29 사상 최고 $5,595</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">1~9월 순매수 1위</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #30D158;">폴란드 123t</div>
              <div style="font-size: 0.68rem; color: #30D158;">9월 한 달 25t · 같은 달 중국은 23t</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">한국은행 금고</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FF453A;">104.4톤</div>
              <div style="font-size: 0.68rem; color: #FF453A;">외환보유액의 1.1%(6월 말) · 실물 매입 13년째 없음</div>
            </div>
          `;
        }
      } else if (dateStr === '20261031') {
        if (img) img.src = 'https://lh3.googleusercontent.com/d/1pMn7U7j2JUPtHkuE8JBmmbUyxd2LFu7V';
        if (webp) webp.srcset = 'images/editorial_cartoon_20261031.webp';
        if (downloadBtn) {
          downloadBtn.href = 'https://lh3.googleusercontent.com/d/1pMn7U7j2JUPtHkuE8JBmmbUyxd2LFu7V';
          downloadBtn.download = 'RYUYOUNGSUN_Editorial_Cartoon_20261031.png';
        }
        if (dateEl) dateEl.innerText = '2026.10.31 토요일 주말 특급 아카이브';
        if (title) title.innerText = '『"노도강은 행정만 서울일 뿐 생활권은 완전히 탈락했다!" 대서울 역삼각권과 부동산 지도의 거대한 지각변동』';
        if (points) {
          points.innerHTML = `
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">①</span>
              <div><strong>데이터로 증명된 '대서울 역삼각권'과 노도강 탈락:</strong> 소득 9분위 기준 평균 월급 570만 원 이상의 고임금 일자리와 30평대 고가 아파트는 정확히 '2호선 내부 ↔ 경부축-동탄 ↔ 여의도·구로-동탄' 역삼각권과 100% 일치합니다. 노원·도봉·강북 등 북부 외곽은 행정만 서울일 뿐 자본과 일자리 생활권에서 탈락했습니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">②</span>
              <div><strong>GTX 시공간 압축과 동탄 지가 기울기의 법칙:</strong> 킨텍스-서울역 17분 주파 등 광역급행망이 거대한 공간 압축을 이끌지만, 동탄역처럼 역세권 반경 1~2km를 벗어나면 지가가 급락하는 가파른 기울기를 보입니다. 복합개발과 지선을 잇는 허브 앤 스포크(Hub & Spoke)가 핵심입니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">③</span>
              <div><strong>직접 경제(Face-to-Face)의 불변성과 자산 압축:</strong> AI·통신 기술 고도화에도 대면 네트워킹과 아이디어 교류의 가치는 대체 불가능합니다. 껍데기 행정구역 간판에 속지 말고, 일자리와 급행망이 관통하는 대서울 역삼각권 핵심 축으로 자산을 압축해야 합니다.</div>
            </div>
          `;
        }
        if (factGrid) {
          factGrid.innerHTML = `
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">서울 핵심 산업 비중</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #0A84FF;">25%</div>
              <div style="font-size: 0.68rem; color: #30D158;">금융 13% + IT 12% 독점</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">고임금 일자리 기준</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FFD60A;">월 570만 원+</div>
              <div style="font-size: 0.68rem; color: #FFD60A;">소득 9~10분위 역삼각 집중</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">GTX 시공간 압축</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #30D158;">단 17분 주파</div>
              <div style="font-size: 0.68rem; color: #30D158;">킨텍스 ↔ 서울역 1시간 단축</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">동탄역 지가 유효반경</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FF453A;">1~2km 한계</div>
              <div style="font-size: 0.68rem; color: #FF453A;">외곽 급격한 지가 하락 기울기</div>
            </div>
          `;
        }
      } else if (dateStr === '20261030') {
        if (img) img.src = 'https://lh3.googleusercontent.com/d/1hYKsK-I82lTaXVdEgxgdyMogpop8gGdZ';
        if (webp) webp.srcset = 'images/editorial_cartoon_20261030.webp';
        if (downloadBtn) {
          downloadBtn.href = 'https://lh3.googleusercontent.com/d/1hYKsK-I82lTaXVdEgxgdyMogpop8gGdZ';
          downloadBtn.download = 'RYUYOUNGSUN_Editorial_Cartoon_20261030.png';
        }
        if (dateEl) dateEl.innerText = '2026.10.30 07:00 조간 정밀 팩트 확정치 반영';
        if (title) title.innerText = '『구글의 1,950억 달러 늪과 제국을 삼키는 AI 자기잠식(Cannibalization)의 저주』';
        if (points) {
          points.innerHTML = `
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">①</span>
              <div><strong>사상 최대 실적의 허울과 90억 달러 현금 증발:</strong> 3분기 매출 1,276억 달러(+25%), 클라우드 158억 달러(+103%)에도 잉여현금흐름(FCF)이 -90.7억 달러로 적자 전환하며 알파벳 주가는 -12.64% 폭락했습니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">②</span>
              <div><strong>AI 검색의 역설과 '자기잠식(Cannibalization)':</strong> 생성형 AI 에이전트가 답을 직접 해결할수록, 10개 파란 링크 클릭당 과금하던 기존 검색광고(비중 74.2%) 모델은 스스로 해체될 운명입니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">③</span>
              <div><strong>클라우드의 역설:</strong> 구글 TPU와 클라우드를 대량 구매한 핵심 고객은 숙적인 오픈AI와 앤트로픽으로, 플랫폼 독점자가 하청 유틸리티로 밀려났습니다.</div>
            </div>
          `;
        }
        if (factGrid) {
          factGrid.innerHTML = `
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">알파벳 3분기 FCF</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FF453A;">-90.7억 달러</div>
              <div style="font-size: 0.68rem; color: #FF453A;">▼ 시장 충격 적자 전환</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">연간 CapEx 설비투자</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FF9F0A;">1,950~2,050억$</div>
              <div style="font-size: 0.68rem; color: #FF9F0A;">AI 인프라 블랙홀</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">알파벳A 실적발표 주가</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FF453A;">▼ 12.64%</div>
              <div style="font-size: 0.68rem; color: #FF453A;">2년 만의 최대 낙폭</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">검색광고 매출 비중</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #0A84FF;">74.2%</div>
              <div style="font-size: 0.68rem; color: #A1A1AA;">AI 자기잠식 노출도</div>
            </div>
          `;
        }
      } else if (dateStr === '20261029') {
        if (img) img.src = 'https://lh3.googleusercontent.com/d/1LuXn4phHeY23tncQDnUR5cN8gM03RSaH';
        if (webp) webp.srcset = 'images/editorial_cartoon_20261029.webp';
        if (downloadBtn) {
          downloadBtn.href = 'https://lh3.googleusercontent.com/d/1LuXn4phHeY23tncQDnUR5cN8gM03RSaH';
          downloadBtn.download = 'RYUYOUNGSUN_Editorial_Cartoon_20261029.png';
        }
        if (dateEl) dateEl.innerText = '2026.10.29 16:30 장 마감 정밀 팩트 확정치';
        if (title) title.innerText = '『코스피 9,200선 고점 돌파 후 6,000선 숨고르기와 1,336원 환율 수급 밸런스』';
        if (points) {
          points.innerHTML = `
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">①</span>
              <div><strong>코스피 6,000선 안착 공방:</strong> 사상 최고치 돌파 후 차익 실현을 거쳐 5,937.66p로 6,000선 안착과 새로운 지지력을 다지고 있습니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">②</span>
              <div><strong>원/달러 1,336원의 균형:</strong> 월말 네고물량과 당국 경계감으로 1,336원대에서 안정적인 수급 균형을 유지하고 있습니다.</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <span style="color: #10B981; font-weight: 800;">③</span>
              <div><strong>글로벌 펀더멘털 재편:</strong> 연준의 점진적 피벗 하에서 실질 FCF가 검증된 퀄리티 자산군으로 유동성이 재편되고 있습니다.</div>
            </div>
          `;
        }
        if (factGrid) {
          factGrid.innerHTML = `
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">코스피 종가</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #38bdf8;">5,937.66p</div>
              <div style="font-size: 0.68rem; color: #38bdf8;">▼ 74.78p (-1.24%)</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">원/달러 마감</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #FF9F0A;">1,336.80원</div>
              <div style="font-size: 0.68rem; color: #FF9F0A;">수급 균형 안정</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">한은 기준금리</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #0A84FF;">3.00%</div>
              <div style="font-size: 0.68rem; color: #A1A1AA;">10월 동결 확정</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 10px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05);">
              <div style="font-size: 0.72rem; color: #86868B;">국고채 10Y-3Y</div>
              <div style="font-size: 1.05rem; font-weight: 800; color: #10B981;">+31.5bp</div>
              <div style="font-size: 0.68rem; color: #10B981;">우상향 정상화</div>
            </div>
          `;
        }
      } else if (dateStr === '20261028') {
        if (img) img.src = 'https://lh3.googleusercontent.com/d/12lC6GDxfJ719IYLNUaqOJ6_QwNv8HdSs';
        if (webp) webp.srcset = 'images/editorial_cartoon_20261028.webp';
        if (downloadBtn) {
          downloadBtn.href = 'https://lh3.googleusercontent.com/d/12lC6GDxfJ719IYLNUaqOJ6_QwNv8HdSs';
          downloadBtn.download = 'RYUYOUNGSUN_Editorial_Cartoon_20261028.png';
        }
        if (dateEl) dateEl.innerText = '2026.10.28 특급 아카이브';
        if (title) title.innerText = '『한은 vs 연준: 1,336원 환율 줄다리기와 한미 금리차 100bp 공방』';
      }
    };

    // 초기화 시 렌더링
    try {
      window.renderFourPollsChart(4, 'all');
      window.updateInflectionBriefCard(4);
    } catch(e) { console.error('Poll chart init error:', e); }

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
      setTimeout(() => { try { window.renderFourPollsChart(4, 'all'); window.updateInflectionBriefCard(4); } catch(e){} }, 100);
    } else {
      document.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => { try { window.renderFourPollsChart(4, 'all'); window.updateInflectionBriefCard(4); } catch(e){} }, 100);
      });
    }
    

  // ==========================================================================
  // 🎵 🎬 CULTURE & KNOWLEDGE DYNAMIC AMBIENT ENGINE (음악·영화 & 지식 앰비언트 엔진)
  // ==========================================================================
  const CULTURE_AMBIENT_ITEMS = [
  {
    "category": "🎵 8090 가요 클래식",
    "cat_key": "music",
    "title": "홍성민 <기억날 그날이 와도> (1990)",
    "desc": "8090 서정 가요의 독보적인 금자탑. 애절한 미성과 담백한 멜로디가 빚어낸 한국 대중음악사의 불멸의 클래식 명곡.",
    "tag": "#8090가요 #불멸의명곡 #홍성민",
    "accent_type": "music",
    "color": "#EC4899",
    "url": "https://youtu.be/WbbQ69dh47M",
    "insight": "시대가 흘러도 변치 않는 멜로디의 힘. 영선 님의 최애곡이자 한국 가요의 황금기를 증명하는 서정시."
  },
  {
    "category": "🎵 포크 & 청춘의 서정",
    "cat_key": "music",
    "title": "동물원 <거리에서> · <흐린 가을 하늘에 편지를>",
    "desc": "김광석과 김창기의 목소리로 기억되는 청춘의 골목길. 화려한 기교 없이 진심 어린 어쿠스틱 선율로 시대를 위로한 명반.",
    "tag": "#동물원 #김광석 #거리에서 #포크음악",
    "accent_type": "music",
    "color": "#38BDF8",
    "url": "https://youtu.be/5ThEW8WYoik",
    "insight": "차가운 도시의 아스팔트 위에서 가을의 쓸쓸함과 따스한 온기를 동시에 길어 올리는 한국 포크의 영혼."
  },
  {
    "category": "🎵 90년대 모던 가요 혁신",
    "cat_key": "music",
    "title": "015B <아주 오래된 연인들> · <이젠 안녕>",
    "desc": "한국 최초의 객원가수 시스템 도입과 하우스 리듬의 파격적 접목. 90년대 트렌드를 선도하며 가요계의 문법을 바꾼 사운드.",
    "tag": "#015B #공일오비 #정석원 #장호일 #모던가요",
    "accent_type": "music",
    "color": "#A855F7",
    "url": "https://youtu.be/S_S0jKvsP50",
    "insight": "프로듀서 중심의 음악 혁명. 세련된 신시사이저와 일상적 가사로 신세대의 감성을 완벽히 포착한 명작."
  },
  {
    "category": "🎵 어쿠스틱 포크 듀오",
    "cat_key": "music",
    "title": "해바라기 <행복을 주는 사람> · <사랑으로>",
    "desc": "이주호의 맑은 통기타와 완벽한 보컬 하모니. 세대를 초월하여 인간애와 희망을 전하는 국민적 힐링 클래식.",
    "tag": "#해바라기 #이주호 #행복을주는사람 #사랑으로",
    "accent_type": "music",
    "color": "#FBBF24",
    "url": "https://youtu.be/8T4zkewkyfA",
    "insight": "단순한 통기타 두 대와 화음만으로 공간 전체를 평온으로 채우는 어쿠스틱 음악의 정수."
  },
  {
    "category": "🎸 글로벌 록 오페라",
    "cat_key": "music",
    "title": "퀸(Queen) <보헤미안 랩소디 (Bohemian Rhapsody)>",
    "desc": "라디오 PD가 6분짜리 곡은 절대 안 뜬다고 잘랐으나, 규칙을 부수고 탄생한 전설. 아카펠라·발라드·오페라·하드록의 완벽한 융합.",
    "tag": "#Queen #프레디머큐리 #보헤미안랩소디 #PSB",
    "accent_type": "music",
    "color": "#F43F5E",
    "url": "https://youtu.be/fJ9rUzIMcZQ",
    "insight": "연구소 지식 아카이브 『D+73 #PSB #소셜리스닝』 연계: 세상의 관습을 깬 과감한 고집이 불멸의 예술을 만든다."
  },
  {
    "category": "🎷 월드뮤직 아카이브",
    "cat_key": "music",
    "title": "지중해와 남미의 선율: 그리스 렘베티카 & 탱고·보사노바",
    "desc": "동서양의 문명이 교차하는 그리스 음악부터 아스토르 피아졸라의 누에보 탱고, 안토니오 카를로스 조빔의 보사노바까지의 문명사적 여정.",
    "tag": "#월드뮤직도슨트 #탱고 #보사노바 #문명사",
    "accent_type": "music",
    "color": "#10B981",
    "url": "https://app.notion.com/p/138e42c8c5e2801abffdc6af10d33236",
    "insight": "연구소 『월드뮤직 도슨트』 연계: 음악은 인류가 국경과 역사의 상처를 건너 소통해 온 가장 아름다운 언어."
  },
  {
    "category": "🎬 밀리터리 시네마 명작",
    "cat_key": "movie",
    "title": "스티븐 스필버그 <라이언 일병 구하기> (Saving Private Ryan)",
    "desc": "오마하 비치 상륙작전 24분의 전율. 영웅주의를 배제하고 전쟁의 공포와 인간의 존엄성을 극사실적으로 증언한 영화사의 걸작.",
    "tag": "#영화 #라이언일병구하기 #스필버그 #밀리터리",
    "accent_type": "movie",
    "color": "#EF4444",
    "url": "https://youtu.be/Hz1guTJDy-I",
    "insight": "스티븐 스필버그 감독 아카데미 5관왕: 오마하 비치 24분의 전율과 전장의 진실을 웅변하는 걸작."
  },
  {
    "category": "🎬 전쟁사 실화 걸작",
    "cat_key": "movie",
    "title": "리들리 스콧 <블랙호크 다운> & <밴드 오브 브라더스>",
    "desc": "1993년 모가디슈의 처절한 15시간과 101공수사단 이지중대의 노르망디 실전 고증. 현대 군사학과 전술 교본이 된 기념비적 영상.",
    "tag": "#블랙호크다운 #밴드오브브라더스 #전술고증 #전우애",
    "accent_type": "movie",
    "color": "#F97316",
    "url": "https://youtu.be/SAl0LMED49E",
    "insight": "아비규환 속에서도 동료를 두고 가지 않는 'No Man Left Behind'의 숭고한 전우애와 현대전의 냉혹함."
  },
  {
    "category": "🎬 칸 황금종려상 & 공간사회학",
    "cat_key": "movie",
    "title": "봉준호 감독 <기생충 (Parasite)>: 공간과 냄새의 사회학",
    "desc": "반지하에서 언덕 위 대저택으로 이어지는 수직적 계단. '가장 좋은 계획은 무계획'이라는 대사가 던진 자본주의의 민낯과 현대 사회학.",
    "tag": "#기생충 #봉준호 #공간경제학 #PSB #자본주의",
    "accent_type": "movie",
    "color": "#8B5CF6",
    "url": "https://app.notion.com/p/F-128-PSB-173e42c8c5e28029a52aff1e498ad1e8",
    "insight": "연구소 『F+128 #PSB #작심삼일』 및 도시공간론 연계: 공간의 배치가 곧 인간의 운명을 규정한다는 영화적 통찰."
  },
  {
    "category": "🎬 문화콘텐츠 & 스토리텔링",
    "cat_key": "movie",
    "title": "왜 사람들은 기능보다 스토리에 돈을 쓸까?: 내러티브의 힘",
    "desc": "스타워즈, 대부, 반지의 제왕이 증명한 조셉 캠벨의 영웅 서사. 이성이 아닌 감정을 움직이는 시네마틱 스토리텔링의 절대 법칙.",
    "tag": "#문화콘텐츠 #스토리텔링 #영화미학 #영웅의여정",
    "accent_type": "movie",
    "color": "#06B6D4",
    "url": "https://app.notion.com/p/263e42c8c5e28059b49fef618af94474",
    "insight": "연구소 지식 아카이브 『참고자료(🔠문화콘텐츠)』 연계: 소비자는 상품이 아니라 그 안에 담긴 서사를 구매한다."
  },
  {
    "category": "📐 10/31 메인 단독 기획",
    "cat_key": "knowledge",
    "title": "대서울 역삼각권과 노도강 탈락의 충격적 진실",
    "desc": "소득 9~10분위(월 570만 이상) 일자리와 30평대 고가 아파트의 100% 일치. 2호선 도심 ↔ 경부축 동탄 ↔ 여의도·구로 역삼각 개발축 검증.",
    "tag": "#대서울역삼각권 #노도강탈락 #김경민교수 #GTX압축",
    "accent_type": "knowledge",
    "color": "#38BDF8",
    "url": "#lead",
    "insight": "서울대학교 김경민 교수 빅데이터 모델 연계: 행정구역 간판이 아닌 일자리와 급행 교통망으로 자산을 압축하라."
  },
  {
    "category": "🔥 글로벌 빅테크 심층 진단",
    "cat_key": "knowledge",
    "title": "구글은 성장하는데 왜 주가는 급락했나?",
    "desc": "알파벳 3분기 FCF -90.7억 달러 처참 붕괴와 2,050억 달러 CapEx 늪. AI 검색이 기존 검색광고를 갉아먹는 자기잠식(Cannibalization)의 저주.",
    "tag": "#구글실적쇼크 #CapEx블랙홀 #AI자기잠식 #빅테크",
    "accent_type": "knowledge",
    "color": "#F97316",
    "url": "#lead",
    "insight": "혁신의 칼날이 자신의 젖줄을 겨누는 모순. 플랫폼 지배력 상실 후 단순 연산 하청 유틸리티로 전락하는 공룡의 비극."
  },
  {
    "category": "📊 매크로 전광판 결산",
    "cat_key": "knowledge",
    "title": "코스피 5,730.74p 마감과 1,334.30원 외환 안전판",
    "desc": "오전 10:05 매도 사이드카 발동(5,599p 저점) 후 개인 1.5조 순매수 및 외인 선물 5,099억 매수로 5,730선 회복. 환율 1,334.30원 안정.",
    "tag": "#코스피5730 #사이드카반등 #환율1334 #외환안전판",
    "accent_type": "knowledge",
    "color": "#10B981",
    "url": "#editorial",
    "insight": "주가 급락 속에서도 외환보유액 4,199억 달러와 원/달러 1,334원선이 든든한 방어벽이 되어 시스템 리스크 차단."
  },
  {
    "category": "🏛️ 30대 사상가의 지혜",
    "cat_key": "knowledge",
    "title": "토마 피케티 『21세기 자본』: r > g의 불평등 공식",
    "desc": "자본수익률(r)이 경제성장률(g)을 앞설 때 부의 대물림과 자산 격차는 구조적으로 심화된다. 300년 계량 데이터를 집대성한 현대 경제학의 고전.",
    "tag": "#토마피케티 #21세기자본 #r대g #불평등동학",
    "accent_type": "knowledge",
    "color": "#EAB308",
    "url": "#masters-wisdom",
    "insight": "노동소득만으로는 자본의 증식 속도를 따라잡을 수 없는 시대, 자산 포트폴리오의 체계적 구축이 필수적인 이유."
  },
  {
    "category": "🏛️ 30대 사상가의 지혜",
    "cat_key": "knowledge",
    "title": "조지프 슘페터: '창조적 파괴(Creative Destruction)'",
    "desc": "자본주의를 전진시키는 진정한 원동력은 가격 경쟁이 아니라 낡은 구조를 파괴하고 새로운 가치를 창출하는 혁신가의 '기업가 정신'.",
    "tag": "#조지프슘페터 #창조적파괴 #기업가정신 #혁신사이클",
    "accent_type": "knowledge",
    "color": "#A855F7",
    "url": "#masters-wisdom",
    "insight": "AI와 로보틱스가 몰고 오는 지각변동 속에서 기존 질서에 안주하는 기업은 도태되고 파괴적 혁신자만이 생존한다."
  },
  {
    "category": "🛡️ 거시경제 리서치",
    "cat_key": "knowledge",
    "title": "가계부채 92.8% 연착륙과 서울 PIR 13.8배 수렴",
    "desc": "GDP 대비 가계부채 105.8% 정점에서 92.8%로 디레버리징 순항. 스트레스 DSR 2단계 정책으로 부동산 거품의 연착륙 경로 구축.",
    "tag": "#가계부채 #PIR13배 #디레버리징 #거시건전성",
    "accent_type": "knowledge",
    "color": "#06B6D4",
    "url": "#macro-debt-lab",
    "insight": "영선 님의 연구소 『국가부채/가계부채』 아카이브 연계: 무리한 영끌을 걷어내고 펀더멘털에 기반한 실물 자산으로의 재편."
  }
];

  let currentCultureAmbientIdx = 0;
  let cultureAmbientTimer = null;
  let cultureAmbientProgressInterval = null;
  let isCultureAmbientPlaying = true;
  let cultureProgressPercent = 0;

  function renderCultureAmbientSlide(idx) {
    const item = CULTURE_AMBIENT_ITEMS[idx];
    if (!item) return;

    const widget = document.getElementById('cultureAmbientWidget');
    const badge = document.getElementById('ambientCategoryBadge');
    const counter = document.getElementById('ambientCounter');
    const title = document.getElementById('ambientTitle');
    const desc = document.getElementById('ambientDesc');
    const tag = document.getElementById('ambientTag');
    const accent = document.getElementById('ambientVisualAccent');

    if (badge) badge.innerText = item.category;
    if (counter) counter.innerText = (idx + 1).toString().padStart(2, '0') + ' / ' + CULTURE_AMBIENT_ITEMS.length.toString().padStart(2, '0');
    if (title) title.innerText = item.title;
    if (desc) desc.innerText = item.desc;
    if (tag) tag.innerText = item.tag;

    if (accent) {
      if (item.cat_key === 'music') {
        accent.innerHTML = '<div class="music-eq-wave"><span></span><span></span><span></span><span></span><span></span></div>';
        accent.style.borderColor = 'rgba(236, 72, 153, 0.4)';
      } else if (item.cat_key === 'movie') {
        accent.innerHTML = '<span style="font-size: 1.4rem;">🎬</span>';
        accent.style.borderColor = 'rgba(249, 115, 22, 0.4)';
      } else {
        accent.innerHTML = '<span style="font-size: 1.4rem;">💡</span>';
        accent.style.borderColor = 'rgba(56, 189, 248, 0.4)';
      }
    }

    if (widget) {
      widget.classList.add('active');
    }
    resetCultureAmbientProgress();
  }

  function resetCultureAmbientProgress() {
    cultureProgressPercent = 0;
    const bar = document.getElementById('ambientProgressFill');
    if (bar) bar.style.width = '0%';
  }

  function startCultureAmbientProgress() {
    clearInterval(cultureAmbientProgressInterval);
    const duration = 10000; // 10 seconds per slide
    const step = 100;
    const increment = (step / duration) * 100;

    cultureAmbientProgressInterval = setInterval(() => {
      if (!isCultureAmbientPlaying) return;
      cultureProgressPercent += increment;
      const bar = document.getElementById('ambientProgressFill');
      if (bar) bar.style.width = Math.min(100, cultureProgressPercent) + '%';

      if (cultureProgressPercent >= 100) {
        nextCultureAmbientSlide();
      }
    }, step);
  }

  function nextCultureAmbientSlide() {
    currentCultureAmbientIdx = (currentCultureAmbientIdx + 1) % CULTURE_AMBIENT_ITEMS.length;
    renderCultureAmbientSlide(currentCultureAmbientIdx);
  }

  function prevCultureAmbientSlide() {
    currentCultureAmbientIdx = (currentCultureAmbientIdx - 1 + CULTURE_AMBIENT_ITEMS.length) % CULTURE_AMBIENT_ITEMS.length;
    renderCultureAmbientSlide(currentCultureAmbientIdx);
  }

  function toggleCultureAmbientAutoPlay() {
    isCultureAmbientPlaying = !isCultureAmbientPlaying;
    const btn = document.getElementById('ambientPlayPauseBtn');
    if (btn) btn.innerText = isCultureAmbientPlaying ? '⏸' : '▶';
  }

  function dismissCultureAmbient() {
    const widget = document.getElementById('cultureAmbientWidget');
    if (widget) widget.classList.remove('active');
    clearInterval(cultureAmbientProgressInterval);
    isCultureAmbientPlaying = false;
  }

  function openCultureItemModal(targetIdx = null) {
    const idx = (targetIdx !== null) ? targetIdx : currentCultureAmbientIdx;
    const item = CULTURE_AMBIENT_ITEMS[idx];
    if (!item) return;

    const modal = document.getElementById('cultureAmbientModal');
    document.getElementById('modalCategoryBadge').innerText = item.category;
    document.getElementById('modalCounterBadge').innerText = (idx + 1) + ' / ' + CULTURE_AMBIENT_ITEMS.length;
    document.getElementById('modalTitle').innerText = item.title;
    document.getElementById('modalDesc').innerText = item.desc;
    document.getElementById('modalInsight').innerText = item.insight;
    document.getElementById('modalTags').innerText = item.tag;

    const actionLink = document.getElementById('modalActionLink');
    if (actionLink) {
      actionLink.href = item.url;
      if (item.cat_key === 'music') {
        actionLink.innerText = '🎧 명곡 감상하기 ↗';
      } else if (item.cat_key === 'movie') {
        actionLink.innerText = '🎬 시네마 영상/아카이브 열기 ↗';
      } else {
        actionLink.innerText = '📖 지식 아카이브 / 리포트 보기 ↗';
      }
    }

    if (modal) modal.classList.add('active');
  }

  function closeCultureItemModal() {
    const modal = document.getElementById('cultureAmbientModal');
    if (modal) modal.classList.remove('active');
  }

  function initCultureAmbientEngine() {
    // Start after 1.5 seconds of page load
    setTimeout(() => {
      renderCultureAmbientSlide(0);
      startCultureAmbientProgress();
    }, 1500);

    // Pause on hover
    const widget = document.getElementById('cultureAmbientWidget');
    if (widget) {
      widget.addEventListener('mouseenter', () => { isCultureAmbientPlaying = false; });
      widget.addEventListener('mouseleave', () => { isCultureAmbientPlaying = true; });
    }
  }

  // Auto initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCultureAmbientEngine);
  } else {
    initCultureAmbientEngine();
  }
