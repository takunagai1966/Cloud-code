# CHANGELOG

このリポジトリに対する主な変更履歴を記録します。

## 2026-09-18（続き2）

- 03_FURNITURE に `04_DESIGN_CONTRACT/` フォルダを新設。デザイナーからの提案（初期開発費200万円・ロイヤリティ3%）と、代表案（頭金なし・ロイヤリティ5%）を損益分岐点（累計売上約1億円）で比較分析し、長期的には提案通り3%を維持する方が有利になり得ることを整理（[DESIGNER_PROPOSAL_ANALYSIS.md](./03_FURNITURE/04_DESIGN_CONTRACT/DESIGNER_PROPOSAL_ANALYSIS.md)）。ロイヤリティ算定基準の明記とシリーズ2の知財帰属条項を契約に盛り込むことを優先課題として記録

## 2026-09-18（続き）

- **【訂正】** シリーズ1の製作パートナーはマレーシアの会社であり、石巻工房は製作パートナーではなくデザイン・ものづくりの思想の**参考モデル**であることを明確化。以前 PARTNER_CANDIDATES.md 等で石巻工房を「製作パートナー候補」としていた記述を訂正し、石巻工房への打診メール案は送付しない参考扱いに変更。
- マレーシアの製作パートナー候補として Takashima Woodwork Sdn. Bhd.（ペラ州、木製家具メーカー、日本市場向け実績あり）をウェブ検索で特定し記録。代表の意図する会社と同一か要確認。

## 2026-09-18

- 03_FURNITURE に `01_PRODUCTS/`・`02_MANUFACTURERS/` フォルダを新設
- 合板 × カムロック接合によるモジュラーシステム家具（棚・ベンチ・デスク）の企画書を作成（[SYSTEM_FURNITURE_CONCEPT.md](./03_FURNITURE/01_PRODUCTS/SYSTEM_FURNITURE_CONCEPT.md)）。USM Haller をベンチマークに、カフェ・オフィス向けの拡張可能な什器システムとして構想
- 製作パートナー候補として石巻工房 (Ishinomaki Laboratory) の情報と打診メール案を整理（[PARTNER_CANDIDATES.md](./03_FURNITURE/02_MANUFACTURERS/PARTNER_CANDIDATES.md)）
- 03_FURNITURE に `03_JOINT_PATENT_RND/` フォルダを新設。USM Haller のジョイント（ボール＋内部拡張スリーブ方式、1965年特許・現在は権利満了）を技術分析し、機構的に異なる次世代ジョイントの候補案（クォーターターン・カム方式ほか）を整理（[USM_JOINT_ANALYSIS_AND_NEXT_GEN_CONCEPT.md](./03_FURNITURE/03_JOINT_PATENT_RND/USM_JOINT_ANALYSIS_AND_NEXT_GEN_CONCEPT.md)）
- システム家具ラインは特許出願前の資料のため、社外共有はNDA締結後に限る旨をREADME・企画書に明記
- 新規ジョイント コンセプトAの分解図（展開図）を追加
- 新規ジョイントの金型費用の概算（ラフな相場感）とパーツ構成（金型要:2点／不要:2点）を USM_JOINT_ANALYSIS_AND_NEXT_GEN_CONCEPT.md に追記
- USM Haller の公式耐荷重仕様（1区画75kg、棚板単体50kg等）を基準に、1棚20kgという目標の見立てと現時点の未検証事項を追記
- **【訂正】** システム家具ラインは合板＋ジョイントの**シリーズ1**と、真鍮＋スチールポール＋スチール板の**シリーズ2**という、素材・構造が全く別の独立した2企画であることを明確化。以前の記述（シリーズ2のフレームに合板パネルを掛ける案）は誤りのため撤回し、シリーズ2は合板を一切使用しない方針に訂正。金型費用（真鍮の製法に合わせ削り出し/精密鋳造ベースに修正）・強度見立て（面材をスチール板に修正）も合わせて訂正し、03_FURNITURE/README.md にシリーズ比較表を追加

## 2026-07-11

- CLAUDE.md を作成し、リポジトリの目的・事業構成・言語方針・将来の連携予定を明文化
- 事業領域ごとの番号付きフォルダ（01_VIVANI〜09_COMPANY_MANUAL）を作成し、各フォルダに用途を説明する README.md を追加
- リポジトリ直下に README.md、COMPANY_PROFILE.md、BUSINESS_POLICY.md、TODO.md、CHANGELOG.md を追加
