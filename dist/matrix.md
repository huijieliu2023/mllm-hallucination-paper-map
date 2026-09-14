# 多模态大模型忠实性：方法分类与文献矩阵（2023—2026）

**版本日期：** 2026 年 9 月 14 日  
**网站当前条目：** 622 篇去重论文；其中 539 篇已链接到指定会议/期刊的官方 proceedings 或出版页面，83 篇保留为 Preprint / venue to verify。核心幻觉论文与相邻忠实性研究在网页中分别标记。
**年份范围：** 2023—2026。2026 条目只有在正式 proceedings 页面可核验时才标注目标会议。

**本轮全量目录扫描：** 2026 年 9 月 14 日按会议与年份重新扫描 ACL、ICML、ICLR、NeurIPS、CVPR、ICCV、ECCV、EMNLP 与 NAACL 的官方目录，并补充 AAAI 官方 OJS、IJCV 出版页面和 WWW 官方/DOI 记录。针对本轮重点复核的 CVPR、ICLR 与 NeurIPS，完整解析 10 个官方年度目录，并对 2,031 个视觉/多模态候选的官方详情页逐篇抓取摘要后分类；最终网页中收录 CVPR 136 篇、ICLR 78 篇、NeurIPS 68 篇。ICML 2023—2025 使用 PMLR 正式卷，2026 使用 ICML 官方日程；ACL 系列使用 ACL Anthology 的主会与 Findings 页面。“核心幻觉”仅保留题名明确研究视觉/多模态幻觉的论文；官方摘要明确讨论幻觉或与视觉证据、感知/推理忠实性、不确定性直接相关的论文标为“相关研究”。NeurIPS 2026 尚无可核验的正式 proceedings，因此不提前将预印本标为 NeurIPS 2026。

## 官方会议/期刊补充（2025—2026）

以下条目以正式 proceedings 页面为链接来源，供网站的指定会议筛选使用；该补充集并不把预印本自动标成已发表。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M133 | 2025 | Nullu | [Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Nullu_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_via_HalluSpace_CVPR_2025_paper.html) | 缓解方法 |
| M134 | 2025 | ICT | [ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ICT_Image-Object_Cross-Level_Trusted_Intervention_for_Mitigating_Object_Hallucination_in_CVPR_2025_paper.html) | 缓解方法 |
| M135 | 2025 | Attention Lens | [Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens](https://openaccess.thecvf.com/content/CVPR2025/html/Jiang_Devils_in_Middle_Layers_of_Large_Vision-Language_Models_Interpreting_Detecting_CVPR_2025_paper.html) | 评价与检测；缓解方法 |
| M136 | 2025 | INTER | [INTER: Mitigating Hallucination in Large Vision-Language Models by Interaction Guidance Sampling](https://openaccess.thecvf.com/content/ICCV2025/html/Dong_INTER_Mitigating_Hallucination_in_Large_Vision-Language_Models_by_Interaction_Guidance_ICCV_2025_paper.html) | 缓解方法 |
| M137 | 2025 | EAZY | [Hallucinatory Image Tokens: A Training-free EAZY Approach to Detecting and Mitigating Object Hallucinations in LVLMs](https://openaccess.thecvf.com/content/ICCV2025/html/Che_Hallucinatory_Image_Tokens_A_Training-free_EAZY_Approach_to_Detecting_and_ICCV_2025_paper.html) | 评价与检测；缓解方法 |
| M138 | 2025 | Context | [Why LVLMs Are More Prone to Hallucinations in Longer Responses: The Role of Context](https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_Why_LVLMs_Are_More_Prone_to_Hallucinations_in_Longer_Responses_ICCV_2025_paper.html) | 评价与检测；缓解方法 |
| M139 | 2026 | VES-RFT | [VES-RFT: Rewarding Visual Evidence Sensitivity to Mitigate Hallucinations in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Hou_VES-RFT_Rewarding_Visual_Evidence_Sensitivity_to_Mitigate_Hallucinations_in_Large_CVPR_2026_paper.html) | 缓解方法 |
| M140 | 2026 | CausalLens | [CausalLens: Sensitivity-Guided Multi-Head Causal Intervention for Hallucination Mitigation in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_CausalLens_Sensitivity-Guided_Multi-Head_Causal_Intervention_for_Hallucination_Mitigation_in_Large_CVPR_2026_paper.html) | 缓解方法 |
| M141 | 2026 | MCoT | [Understanding and Mitigating Hallucinations in Multimodal Chain-of-Thought Models](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Understanding_and_Mitigating_Hallucinations_in_Multimodal_Chain-of-Thought_Models_CVPR_2026_paper.html) | 评价与检测；缓解方法 |
| M142 | 2026 | VEGAS | [VEGAS: Mitigating Hallucinations in Large Vision-Language Models via Vision-Encoder Attention Guided Adaptive Steering](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_VEGAS_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_Vision-Encoder_Attention_CVPRF_2026_paper.html) | 缓解方法 |
| M143 | 2026 | DPA | [Alleviating Hallucinations in Large Vision-Language Models via Decoding-Time Perturbation Adaptation](https://openaccess.thecvf.com/content/CVPR2026F/html/Bai_Alleviating_Hallucinations_in_Large_Vision-Language_Models_via_Decoding-Time_Perturbation_Adaptation_CVPRF_2026_paper.html) | 缓解方法 |
| M144 | 2026 | AIR | [Mitigating Object Hallucinations in LVLMs via Attention Imbalance Rectification](https://openaccess.thecvf.com/content/CVPR2026F/html/Sun_Mitigating_Object_Hallucinations_in_LVLMs_via_Attention_Imbalance_Rectification_CVPRF_2026_paper.html) | 缓解方法 |
| M145 | 2026 | ALEAHallu | [Look Closer! An Adversarial Parametric Editing Framework for Hallucination Mitigation in VLMs](https://ojs.aaai.org/index.php/AAAI/article/download/39336/43297) | 缓解方法 |
| M146 | 2026 | Owl | [Causally-Grounded Dual-Path Attention Intervention for Object Hallucination Mitigation in LVLMs](https://ojs.aaai.org/index.php/AAAI/article/download/40918/44879) | 缓解方法 |
| M147 | 2026 | SAVER | [SAVER: Mitigating Hallucinations in Large Vision-Language Models via Style-Aware Visual Early Revision](https://ojs.aaai.org/index.php/AAAI/article/view/40873) | 缓解方法 |
| M148 | 2025 | Fine-Grained AI Feedback | [Detecting and Mitigating Hallucination in Large Vision Language Models via Fine-Grained AI Feedback](https://ojs.aaai.org/index.php/AAAI/article/view/34744) | 评价与检测；缓解方法 |
| M149 | 2026 | RFI | [RFI: Rectified Flow Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/37320) | 缓解方法 |
| M150 | 2026 | Taming the Phantom | [Taming the Phantom: Token-Asymmetric Filtering for Hallucination Mitigation in Large Vision-Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/37768) | 缓解方法 |
| M151 | 2026 | EchoBat | [EchoBat: Echo-Vision Enhancement and Echo-Layered Sampling for Video LLMs Hallucination Mitigation](https://ojs.aaai.org/index.php/AAAI/article/view/40875) | 缓解方法 |
| M152 | 2025 | SECOND | [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://proceedings.mlr.press/v267/park25c.html) | 缓解方法 |
| M153 | 2024 | HALC | [HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding](https://proceedings.mlr.press/v235/chen24bi.html) | 缓解方法 |
| M154 | 2025 | Common-O | [What’s in Common? Multimodal Models Hallucinate When Reasoning Across Scenes](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3e5b0db387078ac4968fd536d3c3a019-Abstract-Datasets_and_Benchmarks_Track.html) | 评价与检测 |
| M155 | 2025 | CMM | [The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9b0b18a77421d45d26c3df5612caefe7-Abstract-Datasets_and_Benchmarks_Track.html) | 评价与检测 |
| M156 | 2024 | VHTest | [Visual Hallucinations of Multi-modal Large Language Models](https://aclanthology.org/2024.findings-acl.573/) | 评价与检测 |
| M157 | 2024 | VCD | [Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://openaccess.thecvf.com/content/CVPR2024/html/Leng_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_through_Visual_Contrastive_CVPR_2024_paper.html) | 缓解方法 |
| M158 | 2025 | HalLoc | [HalLoc: Token-level Localization of Hallucinations for Vision Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Park_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models_CVPR_2025_paper.html) | 评价与检测 |
| M159 | 2025 | TL-DPO | [Stop Learning it all to Mitigate Visual Hallucination, Focus on the Hallucination Target](https://openaccess.thecvf.com/content/CVPR2025/papers/Yoon_Stop_Learning_it_all_to_Mitigate_Visual_Hallucination_Focus_on_CVPR_2025_paper.pdf) | 缓解方法 |
| M160 | 2025 | Visual Information Steering | [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://proceedings.mlr.press/v267/li25ca.html) | 缓解方法 |
| M161 | 2025 | Image-Grounded Guidance | [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://proceedings.mlr.press/v267/zhao25j.html) | 缓解方法 |
| M162 | 2024 | R-Bench | [Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models](https://proceedings.mlr.press/v235/wu24l.html) | 评价与检测 |
| M163 | 2024 | Object Grounding | [Does Object Grounding Really Reduce Hallucination of Large Vision-Language Models?](https://aclanthology.org/2024.emnlp-main.159/) | 评价与检测 |
| M164 | 2024 | VisDiaHalBench | [VisDiaHalBench: A Visual Dialogue Benchmark For Diagnosing Hallucination in Large Vision-Language Models](https://aclanthology.org/2024.acl-long.658/) | 评价与检测 |
| M165 | 2026 | Textual Embeddings | [Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings](https://aclanthology.org/2026.findings-acl.2086/) | 缓解方法 |
| M166 | 2026 | Vision-Language Introspection | [Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering](https://aclanthology.org/2026.acl-long.1784/) | 缓解方法 |
| M167 | 2025 | SPIN | [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631/) | 缓解方法 |
| M168 | 2025 | MFCD | [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452/) | 缓解方法 |
| M169 | 2025 | SHARP | [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725/) | 缓解方法 |
| M170 | 2025 | EMPO | [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982/) | 缓解方法 |
| M171 | 2025 | ContextualLens | [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://aclanthology.org/2025.naacl-long.488/) | 评价与检测；缓解方法 |
| M172 | 2025 | Summary-Guided Decoding | [Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding](https://aclanthology.org/2025.findings-naacl.235/) | 缓解方法 |
| M173 | 2026 | Anchor-Final | [Anchor-Final Self-Supervision Drives Hallucination-Aware Optimization in Large Vision-Language Models](https://icml.cc/virtual/2026/poster/63887) | 缓解方法 |
| M174 | 2026 | Automatic Layer Selection | [Automatic Layer Selection for Hallucination Detection](https://icml.cc/virtual/2026/poster/61195) | 评价与检测 |
| M175 | 2026 | Spectral Surgery | [Beyond Attention Imbalance: Mitigating Hallucinations via Spectral Surgery](https://icml.cc/virtual/2026/poster/63155) | 缓解方法 |
| M176 | 2026 | Visual Rectification | [Beyond Blind Noising: Disentangled Visual Rectification for Hallucination Mitigation in MLLMs](https://icml.cc/virtual/2026/poster/63609) | 缓解方法 |
| M177 | 2026 | Attention Contrastive Decoding | [Beyond Logits: Coherent Hallucination Mitigation via Attention Contrastive Decoding](https://icml.cc/virtual/2026/poster/63322) | 缓解方法 |
| M178 | 2026 | Conflict-Aware Adaptive Alignment | [Conflict-Aware Adaptive Alignment for LLM Hallucination Mitigation](https://icml.cc/virtual/2026/poster/60877) | 缓解方法 |
| M179 | 2026 | DOUBT | [DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs](https://icml.cc/virtual/2026/poster/64161) | 评价与检测 |
| M180 | 2026 | Efficient Hallucination Detection | [Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads](https://icml.cc/virtual/2026/poster/61700) | 评价与检测 |
| M181 | 2026 | ILVAD | [Finding the Correct Visual Evidence Without Forgetting: Mitigating Hallucination in LVLMs via Inter-Layer Visual Attention Discrepancy](https://icml.cc/virtual/2026/poster/63514) | 缓解方法 |
| M182 | 2026 | OOD-to-Hallucination | [From Out-of-Distribution Detection to Hallucination Detection: A Geometric View](https://icml.cc/virtual/2026/poster/62687) | 评价与检测 |
| M183 | 2026 | HaloProbe | [HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models](https://icml.cc/virtual/2026/poster/62157) | 评价与检测；缓解方法 |
| M184 | 2026 | Reasoning Trajectories | [Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping](https://icml.cc/virtual/2026/poster/62434) | 评价与检测 |
| M185 | 2026 | Instruction Lens Score | [Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucination Detector for Multimodal Large Language Models](https://icml.cc/virtual/2026/poster/62062) | 评价与检测 |
| M186 | 2026 | IRIS | [IRIS: Implicit Reward-Guided Internal Sifting for Mitigating Multimodal Hallucination](https://icml.cc/virtual/2026/poster/60532) | 缓解方法 |
| M187 | 2026 | MEDA | [MEDA: Medical-Oriented Activation Editing for Hallucination Mitigation in Medical Large Vision-Language Model](https://icml.cc/virtual/2026/poster/63562) | 缓解方法 |
| M188 | 2026 | REVIS | [REVIS: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models](https://icml.cc/virtual/2026/poster/65900) | 缓解方法 |
| M189 | 2026 | Visual-Sensitivity Steering | [Steer Where It Matters: Token-Level Visual-Sensitivity Steering for LVLMs Hallucination Mitigation](https://icml.cc/virtual/2026/poster/62374) | 缓解方法 |

本矩阵是综述论文的可追溯证据附表。条目首先由领域综述及其维护的公开文献库形成召回集，再以 arXiv API 核验标题、作者和时间元数据。它是结构化叙述综述的核心样本，不等同于数据库穷尽式系统综述。

## 一、两级方法分类

| 一级功能 | 二级类别 | 数量 | 分类判据 |
|---|---|---:|---|
| 评价与检测 | 封闭探测、综合基准与机制分析 | 28 | 以对象存在性、成对问答或综合诊断为主，兼顾语言先验、幻觉来源和跨模型机制比较。 |
| 评价与检测 | 开放生成与细粒度事实 | 7 | 把自由回答拆成对象、片段、原子事实或场景图三元组，评价可核查主张的支持率。 |
| 评价与检测 | token/主张/内部状态检测 | 7 | 在 token、claim、注意力或隐藏状态层定位错误，并估计置信度或不确定性。 |
| 评价与检测 | 反事实、扰动与开放集 | 4 | 通过反事实编辑、视觉扰动、开放组合或对抗样本检验模型是否真正依赖输入。 |
| 评价与检测 | 视频、音频与长上下文 | 9 | 覆盖动作、事件顺序、场景转移、音视频一致性以及长视频/长上下文累积误差。 |
| 评价与检测 | 专业领域与任务特定评价 | 5 | 面向医疗、事实核查、GUI 等高风险或特定交互任务构建评价协议。 |
| 缓解方法 | 数据、指令与视觉特征训练 | 27 | 通过数据清洗、拒绝错误前提、难负样本、视觉特征增强或训练目标重构来减少幻觉。 |
| 缓解方法 | 偏好对齐与强化学习 | 9 | 使用 DPO、RLHF、RLAIF、奖励模型或细粒度纠错信号，使偏好直接约束证据一致性。 |
| 缓解方法 | 对比解码、logit校准与token控制 | 11 | 在推理时比较视觉/非视觉分布、校准 logit、控制 EOS 或筛选 token，通常无需再训练。 |
| 缓解方法 | 注意力、表示与模型编辑 | 16 | 干预注意力头、隐藏状态、表示子空间或参数方向，以恢复或保持视觉证据。 |
| 缓解方法 | 视觉接地、外部工具与检索增强 | 2 | 调用检测器、检索器、知识源或视觉证据提示，让主张具有可审计的外部支撑。 |
| 缓解方法 | 推理、核验与自我纠错 | 4 | 以分步核验、自反馈、反思、辩论或局部重生成为核心，阻断错误在推理链中传播。 |
| 缓解方法 | 视频与时序专用方法 | 1 | 针对视频动作—场景解耦、时序证据保持和长视频生成设计专门干预。 |

## 二、逐篇方法矩阵

### 评价与检测

#### 封闭探测、综合基准与机制分析（28）

以对象存在性、成对问答或综合诊断为主，兼顾语言先验、幻觉来源和跨模型机制比较。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M001 | 2025 | — | [DeepSeek on a Trip: Inducing Targeted Visual Hallucinations via Representation Vulnerabilities](https://arxiv.org/abs/2502.07905) | 评价与检测 |
| M002 | 2025 | CAOS | [Evaluating Hallucination in Large Vision-Language Models based on Context-Aware Object Similarities](https://arxiv.org/abs/2501.15046) | 评价与检测 |
| M003 | 2025 | HumbleBench | [Measuring Epistemic Humility in Multimodal Large Language Models](https://arxiv.org/abs/2509.09658) | 评价与检测 |
| M004 | 2024 | — | [Delve into Visual Contrastive Decoding for Hallucination Mitigation of Large Vision-Language Models](https://arxiv.org/abs/2412.06775) | 评价与检测 |
| M005 | 2024 | — | [Does Object Grounding Really Reduce Hallucination of Large Vision-Language Models?](https://arxiv.org/abs/2406.14492) | 评价与检测 |
| M006 | 2024 | — | [Who Brings the Frisbee: Probing Hidden Hallucination Factors in Large Vision-Language Model via Causality Analysis](https://arxiv.org/abs/2412.02946) | 评价与检测 |
| M007 | 2024 | AutoHallusion | [AUTOHALLUSION: Automatic Generation of Hallucination Benchmarks for Vision-Language Models](https://arxiv.org/abs/2406.10900) | 评价与检测 |
| M008 | 2024 | CAST | [CAST: Cross-modal Alignment Similarity Test for Vision Language Models](https://arxiv.org/abs/2409.11007) | 评价与检测 |
| M009 | 2024 | H-POPE | [Hierarchical Polling-based Probing Evaluation of Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2411.04077) | 评价与检测 |
| M010 | 2024 | HALLUCINOGEN | [Towards a Systematic Evaluation of Hallucinations in Large-Vision Language Models](https://arxiv.org/abs/2412.20622) | 评价与检测 |
| M011 | 2024 | HaloQuest | [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://arxiv.org/abs/2407.15680) | 评价与检测 |
| M012 | 2024 | HQHBench | [Evaluating the Quality of Hallucination Benchmarks for Large Vision-Language Models](https://arxiv.org/abs/2406.17115) | 评价与检测 |
| M013 | 2024 | Pfram | [Understanding Multimodal Hallucination with Parameter-Free Representation Alignment](https://arxiv.org/abs/2409.01151) | 评价与检测 |
| M014 | 2024 | QL-Bench | [Explore the Hallucination on Low-level Perception for MLLMs](https://arxiv.org/abs/2409.09748) | 评价与检测 |
| M015 | 2024 | Reefknot | [Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2408.09429) | 评价与检测 |
| M016 | 2024 | ROPE | [Multi-Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2407.06192) | 评价与检测 |
| M017 | 2024 | VHExpansion | [Automatically Generating Visual Hallucination Test Cases for Multimodal Large Language Models](https://arxiv.org/abs/2410.11242) | 评价与检测 |
| M018 | 2023 | AMBER | [An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination Evaluation](https://arxiv.org/abs/2311.07397) | 评价与检测 |
| M019 | 2023 | Bingo | [Holistic Analysis of Hallucination in GPT-4V(ision): Bias and Interference Challenges](https://arxiv.org/abs/2311.03287) | 评价与检测 |
| M020 | 2023 | CCEval | [HallE-Switch: Controlling Object Hallucination in Large Vision Language Models](https://arxiv.org/abs/2310.01779) | 评价与检测 |
| M021 | 2023 | CIEM | [CIEM: Contrastive Instruction Evaluation Method for Better Instruction Tuning](https://arxiv.org/abs/2309.02301) | 评价与检测 |
| M022 | 2023 | HaELM | [Evaluation and Analysis of Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2308.15126) | 评价与检测 |
| M023 | 2023 | LRV (GAVIE) | [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://arxiv.org/abs/2306.14565) | 评价与检测 |
| M024 | 2023 | MERLIM | [Behind the Magic, MERLIM: Multi-modal Evaluation Benchmark for Large Image-Language Models](https://arxiv.org/abs/2312.02219) | 评价与检测 |
| M025 | 2023 | MMHal-Bench | [Aligning Large Multimodal Models with Factually Augmented RLHF](https://arxiv.org/abs/2309.14525) | 评价与检测 |
| M026 | 2023 | NOPE | [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338) | 评价与检测 |
| M027 | 2023 | POPE | [Evaluating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2305.10355) | 评价与检测 |
| M028 | 2023 | RAH-Bench | [Mitigating Hallucination in Visual Language Models with Visual Supervision](https://arxiv.org/abs/2311.16479) | 评价与检测 |

#### 开放生成与细粒度事实（7）

把自由回答拆成对象、片段、原子事实或场景图三元组，评价可核查主张的支持率。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M029 | 2025 | F-CLIPScore | [Vision-Encoders (Already) Know What They See: Mitigating Object Hallucination via Simple Fine-Grained CLIPScore](https://arxiv.org/abs/2502.20034) | 评价与检测 |
| M030 | 2024 | — | [Do More Details Always Introduce More Hallucinations in LVLM-based Image Captioning?](https://arxiv.org/abs/2406.12663) | 评价与检测 |
| M031 | 2024 | FIHA | [Autonomous Hallucination Evaluation in Vision-Language Models with Davidson Scene Graphs](https://arxiv.org/abs/2409.13612) | 评价与检测 |
| M032 | 2024 | Tri-He | [Unified Triplet-Level Hallucination Evaluation for Large Vision-Language Models](https://arxiv.org/abs/2410.23114) | 评价与检测 |
| M033 | 2023 | FAITHSCORE | [FAITHSCORE: Evaluating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2311.01477) | 评价与检测 |
| M034 | 2023 | FGHE | [Mitigating Fine-Grained Hallucination by Fine-Tuning Large Vision-Language Models with Caption Rewrites](https://arxiv.org/abs/2312.01701) | 评价与检测 |
| M035 | 2023 | MOCHa (OpenCHAIR) | [MOCHa: Multi-Objective Reinforcement Mitigating Caption Hallucinations](https://arxiv.org/abs/2312.03631) | 评价与检测 |

#### token/主张/内部状态检测（7）

在 token、claim、注意力或隐藏状态层定位错误，并估计置信度或不确定性。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M036 | 2025 | CutPaste&Find | [Efficient Multimodal Hallucination Detector with Visual-aid Knowledge Base](https://arxiv.org/abs/2502.12591) | 评价与检测 |
| M037 | 2025 | HalLoc | [HalLoc: Token-level Localization of Hallucinations for Vision Language Models](https://arxiv.org/abs/2506.10286) | 评价与检测 |
| M038 | 2024 | — | [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://arxiv.org/abs/2411.19187) | 评价与检测 |
| M039 | 2024 | — | [Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens](https://arxiv.org/abs/2411.16724) | 评价与检测 |
| M040 | 2024 | — | [Pre-Training Multimodal Hallucination Detectors with Corrupted Grounding Data](https://arxiv.org/abs/2409.00238) | 评价与检测 |
| M041 | 2024 | DHCP | [Detecting Hallucinations by Cross-modal Attention Pattern in Large Vision-Language Models](https://arxiv.org/abs/2411.18659) | 评价与检测 |
| M042 | 2024 | VL-Uncertainty | [Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation](https://arxiv.org/abs/2411.11919) | 评价与检测 |

#### 反事实、扰动与开放集（4）

通过反事实编辑、视觉扰动、开放组合或对抗样本检验模型是否真正依赖输入。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M043 | 2024 | BEAF | [BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-language Models](https://arxiv.org/abs/2407.13442) | 评价与检测 |
| M044 | 2024 | Hallu-PI | [Hallu-PI: Evaluating Hallucination in Multi-modal Large Language Models within Perturbed Inputs](https://arxiv.org/abs/2408.01355) | 评价与检测 |
| M045 | 2024 | ODE | [Open-Set Evaluation of Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2409.09318) | 评价与检测 |
| M046 | 2023 | HallusionBench | [HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination & Visual Illusion in Large Vision-Language Models](https://arxiv.org/abs/2310.14566) | 评价与检测 |

#### 视频、音频与长上下文（9）

覆盖动作、事件顺序、场景转移、音视频一致性以及长视频/长上下文累积误差。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M047 | 2025 | HAVEN | [Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation](https://arxiv.org/abs/2503.19622) | 评价与检测 |
| M048 | 2025 | UNSCENE | [MASH-VLM:Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871) | 评价与检测；缓解方法 |
| M049 | 2024 | AVHBench | [A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://arxiv.org/abs/2410.18325) | 评价与检测 |
| M050 | 2024 | CMM | [The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio](https://arxiv.org/abs/2410.12787) | 评价与检测 |
| M051 | 2024 | EventHallusion | [Diagnosing Event Hallucinations in Video LLMs](https://arxiv.org/abs/2409.16597) | 评价与检测 |
| M052 | 2024 | LongHalQA | [Long-Context Hallucination Evaluation for MultiModal Large Language Models](https://arxiv.org/abs/2410.09962) | 评价与检测 |
| M053 | 2024 | VideoHallucer | [VideoHallucer: Evaluating Intrinsic and Extrinsic Hallucinations in Large Video-Language Models](https://arxiv.org/abs/2406.16338) | 评价与检测 |
| M054 | 2024 | VidHal | [Benchmarking Temporal Hallucinations in Vision LLMs](https://arxiv.org/abs/2411.16771) | 评价与检测 |
| M055 | 2024 | VidHalluc | [Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding](https://arxiv.org/abs/2412.03735) | 评价与检测 |

#### 专业领域与任务特定评价（5）

面向医疗、事实核查、GUI 等高风险或特定交互任务构建评价协议。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M056 | 2025 | MedHallTune | [An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models](https://arxiv.org/abs/2502.20780) | 评价与检测 |
| M057 | 2024 | Med-HallMark | [Detecting and Evaluating Medical Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2406.10185) | 评价与检测 |
| M058 | 2024 | MedHallBench | [A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://arxiv.org/abs/2412.18947) | 评价与检测 |
| M059 | 2024 | MFC-Bench | [MFC-Bench: Benchmarking Multimodal Fact-Checking with Large Vision-Language Models](https://arxiv.org/abs/2406.11288) | 评价与检测 |
| M060 | 2024 | VGA | [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://arxiv.org/abs/2406.14056) | 评价与检测 |

#### 注意力、表示与模型编辑（1）

干预注意力头、隐藏状态、表示子空间或参数方向，以恢复或保持视觉证据。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M061 | 2025 | UNSCENE | [MASH-VLM:Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871) | 评价与检测；缓解方法 |

### 缓解方法

#### 视频、音频与长上下文（1）

覆盖动作、事件顺序、场景转移、音视频一致性以及长视频/长上下文累积误差。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M062 | 2025 | UNSCENE | [MASH-VLM:Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871) | 评价与检测；缓解方法 |

#### 数据、指令与视觉特征训练（27）

通过数据清洗、拒绝错误前提、难负样本、视觉特征增强或训练目标重构来减少幻觉。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M063 | 2025 | — | [Exploring Causes and Mitigation of Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2502.16842) | 缓解方法 |
| M064 | 2025 | — | [Mitigating Hallucinations on Object Attributes using Multiview Images and Negative Instructions](https://arxiv.org/abs/2501.10011) | 缓解方法 |
| M065 | 2025 | — | [The Role of Background Information in Reducing Object Hallucination in Vision-Language Models: Insights from Cutoff API Prompting](https://arxiv.org/abs/2502.15389) | 缓解方法 |
| M066 | 2025 | CAP | [Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting](https://arxiv.org/abs/2502.08317) | 缓解方法 |
| M067 | 2025 | ClearSight | [Visual Signal Enhancement for Object Hallucination Mitigation in Multimodal Large language Models](https://arxiv.org/abs/2503.13107) | 缓解方法 |
| M068 | 2025 | EAZY | [Eliminating Hallucinations in LVLMs by Zeroing out Hallucinatory Image Tokens](https://arxiv.org/abs/2503.07772) | 缓解方法 |
| M069 | 2025 | HalCECE | [A Framework for Explainable Hallucination Detection through Conceptual Counterfactuals in Image Captioning](https://arxiv.org/abs/2503.00436) | 缓解方法 |
| M070 | 2025 | MFP | [Mitigating Object Hallucinations in MLLMs via Multi-Frequency Perturbations](https://arxiv.org/abs/2503.14895) | 缓解方法 |
| M071 | 2025 | NDE | [Treble Counterfactual VLMs: A Causal Approach to Hallucination](https://arxiv.org/abs/2503.06169) | 缓解方法 |
| M072 | 2025 | PerturboLLaVA | [Reducing Multimodal Hallucinations with Perturbative Visual Training](https://arxiv.org/abs/2503.06486) | 缓解方法 |
| M073 | 2025 | SENTINEL | [Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455) | 缓解方法 |
| M074 | 2025 | TruthPrInt | [Mitigating LVLM Object Hallucination Via Latent Truthful-Guided Pre-Intervention](https://arxiv.org/abs/2503.10602) | 缓解方法 |
| M075 | 2025 | VAP | [Poison as Cure: Visual Noise for Mitigating Object Hallucinations in LVMs](https://arxiv.org/abs/2501.19164) | 缓解方法 |
| M076 | 2025 | VASparse | [Towards Efficient Visual Hallucination Mitigation via Visual-Aware Token Sparsification](https://arxiv.org/abs/2501.06553) | 缓解方法 |
| M077 | 2024 | MagPrompt | [Magnifier Prompt: Tackling Multimodal Hallucination via Extremely Simple Instructions](https://arxiv.org/abs/2410.11701) | 缓解方法 |
| M078 | 2024 | OHD-Caps | [Investigating and Mitigating Object Hallucinations in Pretrained Vision-Language (CLIP) Models](https://arxiv.org/abs/2410.03176) | 缓解方法 |
| M079 | 2024 | PATCH | [From Pixels to Tokens: Revisiting Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2410.06795) | 缓解方法 |
| M080 | 2024 | Verb Mirage | [Unveiling and Assessing Verb Concept Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2412.04939) | 缓解方法 |
| M081 | 2024 | VHD | [Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://arxiv.org/abs/2412.13949) | 缓解方法 |
| M082 | 2024 | VORD | [Visual Ordinal Calibration for Mitigating Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2412.15739) | 缓解方法 |
| M083 | 2023 | HACL | [Hallucination Augmented Contrastive Learning for Multimodal Large Language Model](https://arxiv.org/abs/2312.06968) | 缓解方法 |
| M084 | 2023 | HalDectect | [Detecting and Preventing Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2308.06394) | 缓解方法 |
| M085 | 2023 | HalluciDoctor | [HalluciDoctor: Mitigating Hallucinatory Toxicity in Visual Instruction Data](https://arxiv.org/abs/2311.13614) | 缓解方法 |
| M086 | 2023 | LURE | [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2310.00754) | 缓解方法 |
| M087 | 2023 | OPERA | [OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://arxiv.org/abs/2311.17911) | 缓解方法 |
| M088 | 2023 | VIGC | [VIGC: Visual Instruction Generation and Correction](https://arxiv.org/abs/2308.12714) | 缓解方法 |
| M089 | 2023 | Woodpecker | [Woodpecker: Hallucination Correction for Multimodal Large Language Models](https://arxiv.org/abs/2310.16045) | 缓解方法 |

#### 偏好对齐与强化学习（9）

使用 DPO、RLHF、RLAIF、奖励模型或细粒度纠错信号，使偏好直接约束证据一致性。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M090 | 2025 | LPOI | [LPOI: Listwise Preference Optimization for Vision Language Models](https://arxiv.org/abs/2505.21061) | 缓解方法 |
| M091 | 2025 | OPA-DPO | [Mitigating Hallucinations in Large Vision-Language Models via DPO: On-Policy Data Hold the Key](https://arxiv.org/abs/2501.09695) | 缓解方法 |
| M092 | 2025 | PaMi-VDPO | [PaMi-VDPO: Mitigating Video Hallucinations by Prompt-Aware Multi-Instance Video Preference Learning](https://arxiv.org/abs/2504.05810) | 缓解方法 |
| M093 | 2024 | HDPO | [Mitigating Hallucination in Multimodal Large Language Model via Hallucination-targeted Direct Preference Optimization](https://arxiv.org/abs/2411.10436) | 缓解方法 |
| M094 | 2024 | TPO | [Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation](https://arxiv.org/abs/2412.14487) | 缓解方法 |
| M095 | 2024 | V-DPO | [Mitigating Hallucination in Large Vision Language Models via Vision-Guided Direct Preference Optimization](https://arxiv.org/abs/2411.02712) | 缓解方法 |
| M096 | 2023 | HA-DPO | [Beyond Hallucinations: Enhancing LVLMs through Hallucination-Aware Direct Preference Optimization](https://arxiv.org/abs/2311.16839) | 缓解方法 |
| M097 | 2023 | RLHF-V | [RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback](https://arxiv.org/abs/2312.00849) | 缓解方法 |
| M098 | 2023 | Silkie | [Silkie: Preference Distillation for Large Visual Language Models](https://arxiv.org/abs/2312.10665) | 缓解方法 |

#### 对比解码、logit校准与token控制（11）

在推理时比较视觉/非视觉分布、校准 logit、控制 EOS 或筛选 token，通常无需再训练。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M099 | 2025 | CDAR | [Mitigating Hallucination for Large Vision Language Model by Inter-Modality Correlation Calibration Decoding](https://arxiv.org/abs/2501.01926) | 缓解方法 |
| M100 | 2025 | DeGF | [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2502.06130) | 缓解方法 |
| M101 | 2025 | IFCD | [Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding](https://arxiv.org/abs/2502.01056) | 缓解方法 |
| M102 | 2025 | MINT | [Mitigating Hallucinations in Large Vision-Language Models via Token Reduction](https://arxiv.org/abs/2502.00717) | 缓解方法 |
| M103 | 2025 | Octopus | [Alleviating Hallucination via Dynamic Contrastive Decoding](https://arxiv.org/abs/2503.00361) | 缓解方法 |
| M104 | 2025 | PM | [Through the Magnifying Glass: Adaptive Perception Magnification for Hallucination-Free VLM Decoding](https://arxiv.org/abs/2503.10183) | 缓解方法 |
| M105 | 2024 | CATCH | [Complementary Adaptive Token-level Contrastive Decoding to Mitigate Hallucinations in LVLMs](https://arxiv.org/abs/2411.12713) | 缓解方法 |
| M106 | 2024 | DeCo | [MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://arxiv.org/abs/2410.11779) | 缓解方法 |
| M107 | 2024 | SGD | [Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding](https://arxiv.org/abs/2410.13321) | 缓解方法 |
| M108 | 2024 | VaLiD | [Mitigating the Hallucination of Large Vision Language Models by Visual Layer Fusion Contrastive Decoding](https://arxiv.org/abs/2411.15839) | 缓解方法 |
| M109 | 2023 | VCD | [Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://arxiv.org/abs/2311.16922) | 缓解方法 |

#### 注意力、表示与模型编辑（16）

干预注意力头、隐藏状态、表示子空间或参数方向，以恢复或保持视觉证据。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M110 | 2025 | — | [Mitigating Object Hallucinations in Large Vision-Language Models via Attention Calibration](https://arxiv.org/abs/2502.01969) | 缓解方法 |
| M111 | 2025 | AdaVIB | [Mitigating Hallucinations in Large Vision-Language Models by Adaptively Constraining Information Flow](https://arxiv.org/abs/2502.20750) | 缓解方法 |
| M112 | 2025 | AID | [Attention Hijackers: Detect and Disentangle Attention Hijacking in LVLMs for Hallucination Mitigation](https://arxiv.org/abs/2503.08216) | 缓解方法 |
| M113 | 2025 | AttnReal | [Attention Reallocation: Towards Zero-cost and Controllable Hallucination Mitigation of MLLMs](https://arxiv.org/abs/2503.08342) | 缓解方法 |
| M114 | 2025 | IAVA | [Instruction-Aligned Visual Attention for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2503.18556) | 缓解方法 |
| M115 | 2025 | PAINT | [Fixing Imbalanced Attention to Mitigate In-Context Hallucination of Large Vision-Language Model](https://arxiv.org/abs/2501.12206) | 缓解方法 |
| M116 | 2025 | TARAC | [Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection](https://arxiv.org/abs/2504.04099) | 缓解方法 |
| M117 | 2025 | UNSCENE | [MASH-VLM:Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871) | 评价与检测；缓解方法 |
| M118 | 2025 | VISTA | [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering](https://arxiv.org/abs/2502.03628) | 缓解方法 |
| M119 | 2024 | CausalMM | [Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality](https://arxiv.org/abs/2410.04780) | 缓解方法 |
| M120 | 2024 | CCA | [Mitigating Object Hallucination via Concentric Causal Attention](https://arxiv.org/abs/2410.15926) | 缓解方法 |
| M121 | 2024 | DAMRO | [Dive into the Attention Mechanism of LVLM to Reduce Object Hallucination](https://arxiv.org/abs/2410.04514) | 缓解方法 |
| M122 | 2024 | EAH | [Seeing Clearly by Layer Two: Enhancing Attention Heads to Alleviate Hallucination in LVLMs](https://arxiv.org/abs/2411.09968) | 缓解方法 |
| M123 | 2024 | Nullu | [Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection](https://arxiv.org/abs/2412.13817) | 缓解方法 |
| M124 | 2024 | SIG | [Looking Beyond Text: Reducing Language bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://arxiv.org/abs/2411.14279) | 缓解方法 |
| M125 | 2024 | VTI | [Reducing Hallucinations in Vision-Language Models via Latent Space Steering](https://arxiv.org/abs/2410.15778) | 缓解方法 |

#### 视觉接地、外部工具与检索增强（2）

调用检测器、检索器、知识源或视觉证据提示，让主张具有可审计的外部支撑。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M126 | 2025 | EAGLE | [Enhanced Visual Grounding Minimizes Hallucinations in Instructional Multimodal Models](https://arxiv.org/abs/2501.02699) | 缓解方法 |
| M127 | 2025 | FilterRAG | [Zero-Shot Informed Retrieval-Augmented Generation to Mitigate Hallucinations in VQA](https://arxiv.org/abs/2502.18536) | 缓解方法 |

#### 推理、核验与自我纠错（4）

以分步核验、自反馈、反思、辩论或局部重生成为核心，阻断错误在推理链中传播。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M128 | 2024 | — | [Combating Multimodal LLM Hallucination via Bottom-up Holistic Reasoning](https://arxiv.org/abs/2412.11124) | 缓解方法 |
| M129 | 2024 | MemVR | [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2410.03577) | 缓解方法 |
| M130 | 2024 | VIC | [Thinking Before Looking: Improving Multimodal LLM Reasoning via Mitigating Visual Hallucination](https://arxiv.org/abs/2411.12591) | 缓解方法 |
| M131 | 2023 | Volcano | [Volcano: Mitigating Multimodal Hallucination through Self-Feedback Guided Revision](https://arxiv.org/abs/2311.07362) | 缓解方法 |

#### 视频与时序专用方法（1）

针对视频动作—场景解耦、时序证据保持和长视频生成设计专门干预。

| ID | 年份 | 方法/基准 | 论文 | 功能标签 |
|---:|---:|---|---|---|
| M132 | 2025 | TPC | [Cross-Temporal Prediction Connection for Vision-Language Model Hallucination Reduction](https://arxiv.org/abs/2503.04457) | 缓解方法 |

## 三、使用说明与证据边界

- “评价与检测”包含 benchmark、自动指标、错误定位与机制诊断；“缓解方法”包含训练时、对齐时、解码时、表示层和工具增强干预。
- 分类按论文的主要技术贡献，而不是按唯一机制；同一工作可能同时提供数据集、指标和算法，矩阵以主要贡献归类并保留双功能标签。
- 年份采用 arXiv 首次公开年份。会议录年份与首次预印本年份可能不同；正式投稿时可按目标期刊格式改为会议年份。
- 快速演进领域中预印本占比较高。引用数量不等于证据强度，方法比较仍需检查同行评审状态、代码、数据许可与独立复现。

## 四、去重参考文献（核心矩阵）

1. Kazi Hasan Ibn Arif, Sajib Acharjee Dip, Khizar Hussain, Lang Zhang, Chris Thomas. (2025). [PAINT: Paying Attention to INformed Tokens to Mitigate Hallucination in Large Vision-Language Model](https://arxiv.org/abs/2501.12206). *arXiv:2501.12206*.

2. Kyungho Bae, Jinhyung Kim, Sihaeng Lee, Soonyoung Lee, Gunhee Lee, Jinwoo Choi. (2025). [MASH-VLM: Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871). *arXiv:2503.15871*.

3. Jiaqi Bai, Hongcheng Guo, Zhongyuan Peng, Jian Yang, Zhoujun Li, Mohan Li, et al. (2025). [Mitigating Hallucinations in Large Vision-Language Models by Adaptively Constraining Information Flow](https://arxiv.org/abs/2502.20750). *arXiv:2502.20750*.

4. Assaf Ben-Kish, Moran Yanuka, Morris Alper, Raja Giryes, Hadar Averbuch-Elor. (2023). [Mitigating Open-Vocabulary Caption Hallucinations](https://arxiv.org/abs/2312.03631). *arXiv:2312.03631*.

5. Liwei Che, Tony Qingze Liu, Jing Jia, Weiyi Qin, Ruixiang Tang, Vladimir Pavlovic. (2025). [Hallucinatory Image Tokens: A Training-free EAZY Approach on Detecting and Mitigating Object Hallucinations in LVLMs](https://arxiv.org/abs/2503.07772). *arXiv:2503.07772*.

6. Zhiyang Chen, Yousong Zhu, Yufei Zhan, Zhaowen Li, Chaoyang Zhao, Jinqiao Wang, et al. (2023). [Mitigating Hallucination in Visual Language Models with Visual Supervision](https://arxiv.org/abs/2311.16479). *arXiv:2311.16479*.

7. Jiawei Chen, Dingkang Yang, Tong Wu, Yue Jiang, Xiaolu Hou, Mingcheng Li, et al. (2024). [Detecting and Evaluating Medical Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2406.10185). *arXiv:2406.10185*.

8. Xuweiyi Chen, Ziqiao Ma, Xuejun Zhang, Sihan Xu, Shengyi Qian, Jianing Yang, et al. (2024). [Multi-Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2407.06192). *arXiv:2407.06192*.

9. Beitao Chen, Xinyu Lyu, Lianli Gao, Jingkuan Song, Heng Tao Shen. (2025). [Attention Hijackers: Detect and Disentangle Attention Hijacking in LVLMs for Hallucination Mitigation](https://arxiv.org/abs/2503.08216). *arXiv:2503.08216*.

10. Cong Chen, Mingyu Liu, Chenchen Jing, Yizhou Zhou, Fengyun Rao, Hao Chen, et al. (2025). [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://arxiv.org/abs/2503.06486). *arXiv:2503.06486*.

11. Wey Yeh Choong, Yangyang Guo, Mohan Kankanhalli. (2024). [VidHal: Benchmarking Temporal Hallucinations in Vision LLMs](https://arxiv.org/abs/2411.16771). *arXiv:2411.16771*.

12. Chenhang Cui, Yiyang Zhou, Xinyu Yang, Shirley Wu, Linjun Zhang, James Zou, et al. (2023). [Holistic Analysis of Hallucination in GPT-4V(ision): Bias and Interference Challenges](https://arxiv.org/abs/2311.03287). *arXiv:2311.03287*.

13. Gautier Dagan, Olga Loginova, Anil Batra. (2024). [CAST: Cross-modal Alignment Similarity Test for Vision Language Models](https://arxiv.org/abs/2409.11007). *arXiv:2409.11007*.

14. Shounak Datta, Dhanasekar Sundararaman. (2025). [Evaluating Hallucination in Large Vision-Language Models based on Context-Aware Object Similarities](https://arxiv.org/abs/2501.15046). *arXiv:2501.15046*.

15. Peng Ding, Jingyu Wu, Jun Kuang, Dan Ma, Xuezhi Cao, Xunliang Cai, et al. (2024). [Hallu-PI: Evaluating Hallucination in Multi-modal Large Language Models within Perturbed Inputs](https://arxiv.org/abs/2408.01355). *arXiv:2408.01355*.

16. Xinpeng Ding, Kui Zhang, Jianhua Han, Lanqing Hong, Hang Xu, Xiaomeng Li. (2025). [PaMi-VDPO: Mitigating Video Hallucinations by Prompt-Aware Multi-Instance Video Preference Learning](https://arxiv.org/abs/2504.05810). *arXiv:2504.05810*.

17. Jinhao Duan, Fei Kong, Hao Cheng, James Diffenderfer, Bhavya Kailkhura, Lichao Sun, et al. (2025). [TruthPrInt: Mitigating Large Vision-Language Models Object Hallucination Via Latent Truthful-Guided Pre-Intervention](https://arxiv.org/abs/2503.10602). *arXiv:2503.10602*.

18. Mingqian Feng, Yunlong Tang, Zeliang Zhang, Chenliang Xu. (2024). [Do More Details Always Introduce More Hallucinations in LVLM-based Image Captioning?](https://arxiv.org/abs/2406.12663). *arXiv:2406.12663*.

19. Yuhan Fu, Ruobing Xie, Jiazhen Liu, Bangxiang Lan, Xingwu Sun, Zhanhui Kang, et al. (2024). [Magnifier Prompt: Tackling Multimodal Hallucination via Extremely Simple Instructions](https://arxiv.org/abs/2410.11701). *arXiv:2410.11701*.

20. Yuhan Fu, Ruobing Xie, Xingwu Sun, Zhanhui Kang, Xirong Li. (2024). [Mitigating Hallucination in Multimodal Large Language Model via Hallucination-targeted Direct Preference Optimization](https://arxiv.org/abs/2411.10436). *arXiv:2411.10436*.

21. Hongcheng Gao, Jiashu Qu, Jingyi Tang, Baolong Bi, Yue Liu, Hongyu Chen, et al. (2025). [Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation](https://arxiv.org/abs/2503.19622). *arXiv:2503.19622*.

22. Gregor Geigle, Radu Timofte, Goran Glavaš. (2024). [Does Object Grounding Really Reduce Hallucination of Large Vision-Language Models?](https://arxiv.org/abs/2406.14492). *arXiv:2406.14492*.

23. Xuan Gong, Tianshi Ming, Xinpeng Wang, Zhihua Wei. (2024). [DAMRO: Dive into the Attention Mechanism of LVLM to Reduce Object Hallucination](https://arxiv.org/abs/2410.04514). *arXiv:2410.04514*.

24. Jihao Gu, Yingyao Wang, Meng Cao, Pi Bu, Jun Song, Yancheng He, et al. (2024). [Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation](https://arxiv.org/abs/2412.14487). *arXiv:2412.14487*.

25. Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia Li, Xiaoyu Liu, et al. (2023). [HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models](https://arxiv.org/abs/2310.14566). *arXiv:2310.14566*.

26. Anisha Gunjal, Jihan Yin, Erhan Bas. (2023). [Detecting and Preventing Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2308.06394). *arXiv:2308.06394*.

27. Jinghan He, Kuan Zhu, Haiyun Guo, Junfeng Fang, Zhenglin Hua, Yuheng Jia, et al. (2024). [Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://arxiv.org/abs/2412.13949). *arXiv:2412.13949*.

28. Hongyu Hu, Jiyuan Zhang, Minyi Zhao, Zhenbang Sun. (2023). [CIEM: Contrastive Instruction Evaluation Method for Better Instruction Tuning](https://arxiv.org/abs/2309.02301). *arXiv:2309.02301*.

29. Qidong Huang, Xiaoyi Dong, Pan Zhang, Bin Wang, Conghui He, Jiaqi Wang, et al. (2023). [OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://arxiv.org/abs/2311.17911). *arXiv:2311.17911*.

30. Po-Hsuan Huang, Jeng-Lin Li, Chin-Po Chen, Ming-Ching Chang, Wei-Chao Chen. (2024). [Who Brings the Frisbee: Probing Hidden Hallucination Factors in Large Vision-Language Model via Causality Analysis](https://arxiv.org/abs/2412.02946). *arXiv:2412.02946*.

31. Chashi Mahiul Islam, Samuel Jacob Chacko, Preston Horne, Xiuwen Liu. (2025). [DeepSeek on a Trip: Inducing Targeted Visual Hallucinations via Representation Vulnerabilities](https://arxiv.org/abs/2502.07905). *arXiv:2502.07905*.

32. Chaoya Jiang, Haiyang Xu, Mengfan Dong, Jiaxing Chen, Wei Ye, Ming Yan, et al. (2023). [Hallucination Augmented Contrastive Learning for Multimodal Large Language Model](https://arxiv.org/abs/2312.06968). *arXiv:2312.06968*.

33. Zhangqi Jiang, Junkai Chen, Beier Zhu, Tingjin Luo, Yankun Shen, Xu Yang. (2024). [Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens](https://arxiv.org/abs/2411.16724). *arXiv:2411.16724*.

34. Lei Jiang, Chunzhao Xie, Tongxuan Liu, Yuting Zeng, jinrong Guo, Yunheng Shen, et al. (2025). [TARAC: Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection](https://arxiv.org/abs/2504.04099). *arXiv:2504.04099*.

35. Liqiang Jing, Ruosen Li, Yunmo Chen, Xinya Du. (2023). [FaithScore: Fine-grained Evaluations of Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2311.01477). *arXiv:2311.01477*.

36. Zhehan Kan, Ce Zhang, Zihan Liao, Yapeng Tian, Wenming Yang, Junyuan Xiao, et al. (2024). [CATCH: Complementary Adaptive Token-level Contrastive Decoding to Mitigate Hallucinations in LVLMs](https://arxiv.org/abs/2411.12713). *arXiv:2411.12713*.

37. Seongyun Lee, Sue Hyun Park, Yongrae Jo, Minjoon Seo. (2023). [Volcano: Mitigating Multimodal Hallucination through Self-Feedback Guided Revision](https://arxiv.org/abs/2311.07362). *arXiv:2311.07362*.

38. Yi-Lun Lee, Yi-Hsuan Tsai, Wei-Chen Chiu. (2024). [Delve into Visual Contrastive Decoding for Hallucination Mitigation of Large Vision-Language Models](https://arxiv.org/abs/2412.06775). *arXiv:2412.06775*.

39. Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Li, Shijian Lu, Chunyan Miao, et al. (2023). [Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://arxiv.org/abs/2311.16922). *arXiv:2311.16922*.

40. Sicong Leng, Yun Xing, Zesen Cheng, Yang Zhou, Hang Zhang, Xin Li, et al. (2024). [The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio](https://arxiv.org/abs/2410.12787). *arXiv:2410.12787*.

41. Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Wayne Xin Zhao, Ji-Rong Wen. (2023). [Evaluating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2305.10355). *arXiv:2305.10355*.

42. Lei Li, Zhihui Xie, Mukai Li, Shunian Chen, Peiyi Wang, Liang Chen, et al. (2023). [Silkie: Preference Distillation for Large Visual Language Models](https://arxiv.org/abs/2312.10665). *arXiv:2312.10665*.

43. Chaoyu Li, Eun Woo Im, Pooyan Fazli. (2024). [VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding](https://arxiv.org/abs/2412.03735). *arXiv:2412.03735*.

44. Bin Li, Dehong Gao, Yeyuan Wang, Linbo Jin, Shanqing Yu, Xiaoyan Cai, et al. (2025). [Instruction-Aligned Visual Attention for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2503.18556). *arXiv:2503.18556*.

45. Jiaming Li, Jiacheng Zhang, Zequn Jie, Lin Ma, Guanbin Li. (2025). [Cross-Modal Attention Calibration for LVLM Hallucination Mitigation](https://arxiv.org/abs/2501.01926). *arXiv:2501.01926*.

46. Shuo Li, Jiajun Sun, Guodong Zheng, Xiaoran Fan, Yujiong Shen, Yi Lu, et al. (2025). [Mitigating Object Hallucinations in MLLMs via Multi-Frequency Perturbations](https://arxiv.org/abs/2503.14895). *arXiv:2503.14895*.

47. Zhuowei Li, Haizhou Shi, Yunhe Gao, Di Liu, Zhenting Wang, Yuxiao Chen, et al. (2025). [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models via Visual Information Steering](https://arxiv.org/abs/2502.03628). *arXiv:2502.03628*.

48. Shawn Li, Jiashu Qu, Yuxiao Zhou, Yuehan Qin, Tiankai Yang, Yue Zhao. (2025). [Treble Counterfactual VLMs: A Causal Approach to Hallucination](https://arxiv.org/abs/2503.06169). *arXiv:2503.06169*.

49. Fuxiao Liu, Kevin Lin, Linjie Li, Jianfeng Wang, Yaser Yacoob, Lijuan Wang. (2023). [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://arxiv.org/abs/2306.14565). *arXiv:2306.14565*.

50. Zhongye Liu, Hongbin Liu, Yuepeng Hu, Zedian Shao, Neil Zhenqiang Gong. (2024). [Automatically Generating Visual Hallucination Test Cases for Multimodal Large Language Models](https://arxiv.org/abs/2410.11242). *arXiv:2410.11242*.

51. Yufang Liu, Tao Ji, Changzhi Sun, Yuanbin Wu, Aimin Zhou. (2024). [Investigating and Mitigating Object Hallucinations in Pretrained Vision-Language (CLIP) Models](https://arxiv.org/abs/2410.03176). *arXiv:2410.03176*.

52. Sheng Liu, Haotian Ye, Lei Xing, James Zou. (2024). [Reducing Hallucinations in Vision-Language Models via Latent Space Steering](https://arxiv.org/abs/2410.15778). *arXiv:2410.15778*.

53. Holy Lovenia, Wenliang Dai, Samuel Cahyawijaya, Ziwei Ji, Pascale Fung. (2023). [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338). *arXiv:2310.05338*.

54. Maria Lymperaiou, Giorgos Filandrianos, Angeliki Dimitriou, Athanasios Voulodimos, Giorgos Stamou. (2025). [HalCECE: A Framework for Explainable Hallucination Detection through Conceptual Counterfactuals in Image Captioning](https://arxiv.org/abs/2503.00436). *arXiv:2503.00436*.

55. Shunqi Mao, Chaoyi Zhang, Weidong Cai. (2025). [Through the Magnifying Glass: Adaptive Perception Magnification for Hallucination-Free VLM Decoding](https://arxiv.org/abs/2503.10183). *arXiv:2503.10183*.

56. Ziyang Meng, Yu Dai, Zezheng Gong, Shaoxiong Guo, Minglong Tang, Tongquan Wei. (2024). [VGA: Vision GUI Assistant -- Minimizing Hallucinations through Image-Centric Fine-Tuning](https://arxiv.org/abs/2406.14056). *arXiv:2406.14056*.

57. Kyungmin Min, Minbeom Kim, Kang-il Lee, Dongryeol Lee, Kyomin Jung. (2024). [Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding](https://arxiv.org/abs/2410.13321). *arXiv:2410.13321*.

58. Dexter Neo, Tsuhan Chen. (2024). [VORD: Visual Ordinal Calibration for Mitigating Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2412.15739). *arXiv:2412.15739*.

59. Cong-Duy Nguyen, Xiaobao Wu, Duc Anh Vu, Shuai Zhao, Thong Nguyen, Anh Tuan Luu. (2025). [CutPaste&Find: Efficient Multimodal Hallucination Detector with Visual-aid Knowledge Base](https://arxiv.org/abs/2502.12591). *arXiv:2502.12591*.

60. Hongseok Oh, Wonseok Hwang. (2025). [Do Vision Encoders Truly Explain Object Hallucination?: Mitigating Object Hallucination via Simple Fine-Grained CLIPScore](https://arxiv.org/abs/2502.20034). *arXiv:2502.20034*.

61. Eunkyu Park, Minyeong Kim, Gunhee Kim. (2025). [HalLoc: Token-level Localization of Hallucinations for Vision Language Models](https://arxiv.org/abs/2506.10286). *arXiv:2506.10286*.

62. Shangpin Peng, Senqiao Yang, Li Jiang, Zhuotao Tian. (2025). [Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455). *arXiv:2507.12455*.

63. Nhi Pham, Michael Schott. (2024). [H-POPE: Hierarchical Polling-based Probing Evaluation of Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2411.04077). *arXiv:2411.04077*.

64. Anirudh Phukan,  Divyansh, Harshit Kumar Morj,  Vaishnavi, Apoorv Saxena, Koustava Goswami. (2024). [Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://arxiv.org/abs/2411.19187). *arXiv:2411.19187*.

65. Han Qiu, Jiaxing Huang, Peng Gao, Qin Qi, Xiaoqin Zhang, Ling Shao, et al. (2024). [LongHalQA: Long-Context Hallucination Evaluation for MultiModal Large Language Models](https://arxiv.org/abs/2410.09962). *arXiv:2410.09962*.

66. Nobin Sarwar. (2025). [FilterRAG: Zero-Shot Informed Retrieval-Augmented Generation to Mitigate Hallucinations in VQA](https://arxiv.org/abs/2502.18536). *arXiv:2502.18536*.

67. Ashish Seth, Dinesh Manocha, Chirag Agarwal. (2024). [Towards a Systematic Evaluation of Hallucinations in Large-Vision Language Models](https://arxiv.org/abs/2412.20622). *arXiv:2412.20622*.

68. Yuying Shang, Xinyi Zeng, Yutao Zhu, Xiao Yang, Zhengwei Fang, Jingyuan Zhang, et al. (2024). [From Pixels to Tokens: Revisiting Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2410.06795). *arXiv:2410.06795*.

69. Zhiqing Sun, Sheng Shen, Shengcao Cao, Haotian Liu, Chunyuan Li, Yikang Shen, et al. (2023). [Aligning Large Multimodal Models with Factually Augmented RLHF](https://arxiv.org/abs/2309.14525). *arXiv:2309.14525*.

70. Yinan Sun, Zicheng Zhang, Haoning Wu, Xiaohong Liu, Weisi Lin, Guangtao Zhai, et al. (2024). [Explore the Hallucination on Low-level Perception for MLLMs](https://arxiv.org/abs/2409.09748). *arXiv:2409.09748*.

71. Yaqi Sun, Kyohei Atarashi, Koh Takeuchi, Hisashi Kashima. (2025). [Exploring Causes and Mitigation of Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2502.16842). *arXiv:2502.16842*.

72. Kim Sung-Bin, Oh Hyun-Bin, JungMok Lee, Arda Senocak, Joon Son Chung, Tae-Hyun Oh. (2024). [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://arxiv.org/abs/2410.18325). *arXiv:2410.18325*.

73. Wei Suo, Lijun Zhang, Mengyang Sun, Lin Yuanbo Wu, Peng Wang, Yanning Zhang. (2025). [Octopus: Alleviating Hallucination via Dynamic Contrastive Decoding](https://arxiv.org/abs/2503.00361). *arXiv:2503.00361*.

74. Zhijie Tan, Yuzhi Li, Shengwei Meng, Xiang Yuan, Weiping Li, Tong Mo, et al. (2025). [Mitigating Hallucinations on Object Attributes using Multiview Images and Negative Instructions](https://arxiv.org/abs/2501.10011). *arXiv:2501.10011*.

75. Masayo Tomita, Katsuhiko Hayashi, Tomoyuki Kaneko. (2025). [The Role of Background Information in Reducing Object Hallucination in Vision-Language Models: Insights from Cutoff API Prompting](https://arxiv.org/abs/2502.15389). *arXiv:2502.15389*.

76. Bingkui Tong, Jiaer Xia, Sifeng Shang, Kaiyang Zhou. (2025). [Measuring Epistemic Humility in Multimodal Large Language Models](https://arxiv.org/abs/2509.09658). *arXiv:2509.09658*.

77. Yahan Tu, Rui Hu, Jitao Sang. (2024). [ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2409.09318). *arXiv:2409.09318*.

78. Chongjun Tu, Peng Ye, Dongzhan Zhou, Lei Bai, Gang Yu, Tao Chen, et al. (2025). [Attention Reallocation: Towards Zero-cost and Controllable Hallucination Mitigation of MLLMs](https://arxiv.org/abs/2503.08342). *arXiv:2503.08342*.

79. Andrés Villa, Juan Carlos León Alcázar, Alvaro Soto, Bernard Ghanem. (2023). [Behind the Magic, MERLIM: Multi-modal Evaluation Benchmark for Large Image-Language Models](https://arxiv.org/abs/2312.02219). *arXiv:2312.02219*.

80. Andrés Villa, Juan León Alcázar, Motasem Alfarra, Vladimir Araujo, Alvaro Soto, Bernard Ghanem. (2025). [EAGLE: Enhanced Visual Grounding Minimizes Hallucinations in Instructional Multimodal Models](https://arxiv.org/abs/2501.02699). *arXiv:2501.02699*.

81. Junyang Wang, Yuhang Wang, Guohai Xu, Jing Zhang, Yukai Gu, Haitao Jia, et al. (2023). [AMBER: An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination Evaluation](https://arxiv.org/abs/2311.07397). *arXiv:2311.07397*.

82. Junyang Wang, Yiyang Zhou, Guohai Xu, Pengcheng Shi, Chenlin Zhao, Haiyang Xu, et al. (2023). [Evaluation and Analysis of Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2308.15126). *arXiv:2308.15126*.

83. Lei Wang, Jiabang He, Shenshen Li, Ning Liu, Ee-Peng Lim. (2023). [Mitigating Fine-Grained Hallucination by Fine-Tuning Large Vision-Language Models with Caption Rewrites](https://arxiv.org/abs/2312.01701). *arXiv:2312.01701*.

84. Bin Wang, Fan Wu, Xiao Han, Jiahui Peng, Huaping Zhong, Pan Zhang, et al. (2023). [VIGC: Visual Instruction Generation and Correction](https://arxiv.org/abs/2308.12714). *arXiv:2308.12714*.

85. Zhecan Wang, Garrett Bingham, Adams Yu, Quoc Le, Thang Luong, Golnaz Ghiasi. (2024). [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://arxiv.org/abs/2407.15680). *arXiv:2407.15680*.

86. Shengkang Wang, Hongzhan Lin, Ziyang Luo, Zhen Ye, Guang Chen, Jing Ma. (2024). [MFC-Bench: Benchmarking Multimodal Fact-Checking with Large Vision-Language Models](https://arxiv.org/abs/2406.11288). *arXiv:2406.11288*.

87. Jiaqi Wang, Yifei Gao, Jitao Sang. (2024). [VaLiD: Mitigating the Hallucination of Large Vision Language Models by Visual Layer Fusion Contrastive Decoding](https://arxiv.org/abs/2411.15839). *arXiv:2411.15839*.

88. Chenxi Wang, Xiang Chen, Ningyu Zhang, Bozhong Tian, Haoming Xu, Shumin Deng, et al. (2024). [MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://arxiv.org/abs/2410.11779). *arXiv:2410.11779*.

89. Yueqian Wang, Jianxin Liang, Yuxuan Wang, Huishuai Zhang, Dongyan Zhao. (2024). [Understanding Multimodal Hallucination with Parameter-Free Representation Alignment](https://arxiv.org/abs/2409.01151). *arXiv:2409.01151*.

90. Zehao Wang, Xinpeng Liu, Yudonglin Zhang, Xiaoqian Wu, Zhou Fang, Yifan Fang, et al. (2024). [Verb Mirage: Unveiling and Assessing Verb Concept Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2412.04939). *arXiv:2412.04939*.

91. Yuxuan Wang, Yueqian Wang, Dongyan Zhao, Cihang Xie, Zilong Zheng. (2024). [VideoHallucer: Evaluating Intrinsic and Extrinsic Hallucinations in Large Video-Language Models](https://arxiv.org/abs/2406.16338). *arXiv:2406.16338*.

92. Chao Wang, Weiwei Fu, Yang Zhou. (2025). [TPC: Cross-Temporal Prediction Connection for Vision-Language Model Hallucination Reduction](https://arxiv.org/abs/2503.04457). *arXiv:2503.04457*.

93. Chao Wang, Jianming Yang, Yang Zhou. (2025). [MINT: Mitigating Hallucinations in Large Vision-Language Models via Token Reduction](https://arxiv.org/abs/2502.00717). *arXiv:2502.00717*.

94. Chao Wang, Xuancheng Zhou, Weiwei Fu, Yang Zhou. (2025). [Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding](https://arxiv.org/abs/2502.01056). *arXiv:2502.01056*.

95. Spencer Whitehead, Jacob Phillips, Sean Hendryx. (2024). [Pre-Training Multimodal Hallucination Detectors with Corrupted Grounding Data](https://arxiv.org/abs/2409.00238). *arXiv:2409.00238*.

96. Xiyang Wu, Tianrui Guan, Dianqi Li, Shuaiyi Huang, Xiaoyu Liu, Xijun Wang, et al. (2024). [AutoHallusion: Automatic Generation of Hallucination Benchmarks for Vision-Language Models](https://arxiv.org/abs/2406.10900). *arXiv:2406.10900*.

97. Shengqiong Wu, Hao Fei, Liangming Pan, William Yang Wang, Shuicheng Yan, Tat-Seng Chua. (2024). [Combating Multimodal LLM Hallucination via Bottom-Up Holistic Reasoning](https://arxiv.org/abs/2412.11124). *arXiv:2412.11124*.

98. Junjie Wu, Tsz Ting Chung, Kai Chen, Dit-Yan Yeung. (2024). [Unified Triplet-Level Hallucination Evaluation for Large Vision-Language Models](https://arxiv.org/abs/2410.23114). *arXiv:2410.23114*.

99. Jiarui Wu, Zhuo Liu, Hangfeng He. (2025). [Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting](https://arxiv.org/abs/2502.08317). *arXiv:2502.08317*.

100. Yuxi Xie, Guanzhen Li, Xiao Xu, Min-Yen Kan. (2024). [V-DPO: Mitigating Hallucination in Large Vision Language Models via Vision-Guided Direct Preference Optimization](https://arxiv.org/abs/2411.02712). *arXiv:2411.02712*.

101. Yun Xing, Yiheng Li, Ivan Laptev, Shijian Lu. (2024). [Mitigating Object Hallucination via Concentric Causal Attention](https://arxiv.org/abs/2410.15926). *arXiv:2410.15926*.

102. Bowen Yan, Zhengsong Zhang, Liqiang Jing, Eftekhar Hossain, Xinya Du. (2024). [FIHA: Autonomous Hallucination Evaluation in Vision-Language Models with Davidson Scene Graphs](https://arxiv.org/abs/2409.13612). *arXiv:2409.13612*.

103. Bei Yan, Jie Zhang, Zheng Yuan, Shiguang Shan, Xilin Chen. (2024). [Measuring the Measurers: Quality Evaluation of Hallucination Benchmarks for Large Vision-Language Models](https://arxiv.org/abs/2406.17115). *arXiv:2406.17115*.

104. Qiao Yan, Yuchen Yuan, Xiaowei Hu, Yihan Wang, Jiaqi Xu, Xiwen Wu, et al. (2025). [MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models](https://arxiv.org/abs/2502.20780). *arXiv:2502.20780*.

105. Le Yang, Ziwei Zheng, Boxu Chen, Zhengyu Zhao, Chenhao Lin, Chao Shen. (2024). [Nullu: Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection](https://arxiv.org/abs/2412.13817). *arXiv:2412.13817*.

106. Zhihe Yang, Xufang Luo, Dongqi Han, Yunjian Xu, Dongsheng Li. (2025). [Mitigating Hallucinations in Large Vision-Language Models via DPO: On-Policy Data Hold the Key](https://arxiv.org/abs/2501.09695). *arXiv:2501.09695*.

107. Moon Ye-Bin, Nam Hyeon-Woo, Wonseok Choi, Tae-Hyun Oh. (2024). [BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-language Models](https://arxiv.org/abs/2407.13442). *arXiv:2407.13442*.

108. Shukang Yin, Chaoyou Fu, Sirui Zhao, Tong Xu, Hao Wang, Dianbo Sui, et al. (2023). [Woodpecker: Hallucination Correction for Multimodal Large Language Models](https://arxiv.org/abs/2310.16045). *arXiv:2310.16045*.

109. Hao Yin, Guangzong Si, Zilei Wang. (2025). [ClearSight: Visual Signal Enhancement for Object Hallucination Mitigation in Multimodal Large language Models](https://arxiv.org/abs/2503.13107). *arXiv:2503.13107*.

110. Qifan Yu, Juncheng Li, Longhui Wei, Liang Pang, Wentao Ye, Bosheng Qin, et al. (2023). [HalluciDoctor: Mitigating Hallucinatory Toxicity in Visual Instruction Data](https://arxiv.org/abs/2311.13614). *arXiv:2311.13614*.

111. Tianyu Yu, Yuan Yao, Haoye Zhang, Taiwen He, Yifeng Han, Ganqu Cui, et al. (2023). [RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback](https://arxiv.org/abs/2312.00849). *arXiv:2312.00849*.

112. Fatemeh Pesaran Zadeh, Yoojin Oh, Gunhee Kim. (2025). [LPOI: Listwise Preference Optimization for Vision Language Models](https://arxiv.org/abs/2505.21061). *arXiv:2505.21061*.

113. Bohan Zhai, Shijia Yang, Chenfeng Xu, Sheng Shen, Kurt Keutzer, Chunyuan Li, et al. (2023). [HallE-Control: Controlling Object Hallucination in Large Multimodal Models](https://arxiv.org/abs/2310.01779). *arXiv:2310.01779*.

114. Ruiyang Zhang, Hu Zhang, Zhedong Zheng. (2024). [VL-Uncertainty: Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation](https://arxiv.org/abs/2411.11919). *arXiv:2411.11919*.

115. Yudong Zhang, Ruobing Xie, Xingwu Sun, Yiqing Huang, Jiansheng Chen, Zhanhui Kang, et al. (2024). [DHCP: Detecting Hallucinations by Cross-modal Attention Pattern in Large Vision-Language Models](https://arxiv.org/abs/2411.18659). *arXiv:2411.18659*.

116. Jiacheng Zhang, Yang Jiao, Shaoxiang Chen, Na Zhao, Zhiyu Tan, Hao Li, et al. (2024). [EventHallusion: Diagnosing Event Hallucinations in Video LLMs](https://arxiv.org/abs/2409.16597). *arXiv:2409.16597*.

117. Xiaofeng Zhang, Yihao Quan, Chaochen Gu, Chen Shen, Xiaosong Yuan, Shaotian Yan, et al. (2024). [Seeing Clearly by Layer Two: Enhancing Attention Heads to Alleviate Hallucination in LVLMs](https://arxiv.org/abs/2411.09968). *arXiv:2411.09968*.

118. Kejia Zhang, Keda Tao, Jiasheng Tang, Huan Wang. (2025). [Poison as Cure: Visual Noise for Mitigating Object Hallucinations in LVMs](https://arxiv.org/abs/2501.19164). *arXiv:2501.19164*.

119. Ce Zhang, Zifu Wan, Zhehan Kan, Martin Q. Ma, Simon Stepputtis, Deva Ramanan, et al. (2025). [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2502.06130). *arXiv:2502.06130*.

120. Zhiyuan Zhao, Bin Wang, Linke Ouyang, Xiaoyi Dong, Jiaqi Wang, Conghui He. (2023). [Beyond Hallucinations: Enhancing LVLMs through Hallucination-Aware Direct Preference Optimization](https://arxiv.org/abs/2311.16839). *arXiv:2311.16839*.

121. Haozhe Zhao, Shuzheng Si, Liang Chen, Yichi Zhang, Maosong Sun, Mingjia Zhang, et al. (2024). [Looking Beyond Text: Reducing Language bias in Large Vision-Language Models via Multimodal Dual-Attention and Soft-Image Guidance](https://arxiv.org/abs/2411.14279). *arXiv:2411.14279*.

122. Kening Zheng, Junkai Chen, Yibo Yan, Xin Zou, Xuming Hu. (2024). [Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2408.09429). *arXiv:2408.09429*.

123. Haojie Zheng, Tianyang Xu, Hanchi Sun, Shu Pu, Ruoxi Chen, Lichao Sun. (2024). [Thinking Before Looking: Improving Multimodal LLM Reasoning via Mitigating Visual Hallucination](https://arxiv.org/abs/2411.12591). *arXiv:2411.12591*.

124. Yiyang Zhou, Chenhang Cui, Jaehong Yoon, Linjun Zhang, Zhun Deng, Chelsea Finn, et al. (2023). [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2310.00754). *arXiv:2310.00754*.

125. Guanyu Zhou, Yibo Yan, Xin Zou, Kun Wang, Aiwei Liu, Xuming Hu. (2024). [Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality](https://arxiv.org/abs/2410.04780). *arXiv:2410.04780*.

126. Younan Zhu, Linwei Tao, Minjing Dong, Chang Xu. (2025). [Mitigating Object Hallucinations in Large Vision-Language Models via Attention Calibration](https://arxiv.org/abs/2502.01969). *arXiv:2502.01969*.

127. Xianwei Zhuang, Zhihong Zhu, Yuxin Xie, Liming Liang, Yuexian Zou. (2025). [VASparse: Towards Efficient Visual Hallucination Mitigation via Visual-Aware Token Sparsification](https://arxiv.org/abs/2501.06553). *arXiv:2501.06553*.

128. Xin Zou, Yizhou Wang, Yibo Yan, Yuanhuiyi Lyu, Kening Zheng, Sirui Huang, et al. (2024). [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2410.03577). *arXiv:2410.03577*.

129. Kaiwen Zuo, Yirui Jiang. (2024). [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://arxiv.org/abs/2412.18947). *arXiv:2412.18947*.
