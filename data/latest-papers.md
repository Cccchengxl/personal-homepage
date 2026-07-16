# Latest papers for 程旭丽

Updated: 2026-07-16T07:49:42.071935+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Aromatic Molecule Solvation in Liquid Water with Coupled Cluster Accuracy: The Balance of Pi-Interactions and Hydrophobicity

- Source: arXiv
- Date: 2026-07-14T20:52:10Z
- Venue: physics.chem-ph
- Authors: Nore Stolte, Harald Forbert, Yury Lysogorskiy, Ralf Drautz, Dominik Marx
- Link: https://arxiv.org/abs/2607.13261v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**文章摘要：** 该研究关注水中芳香有机溶质的溶剂化问题。作者指出，疏水溶剂化与定向 O-H...pi 氢键之间存在微妙平衡，而常用力场和先进 DFT 方法难以一致描述这些关键相互作用。论文提出一种数据高效的 upfitting 策略，训练具有 CCSD(T) 精度的机器学习原子间势，用于水溶液芳香分子的凝聚相模拟。
**讨论重点：** 讨论重点是如何用高精度机器学习原子间势描述芳香分子在水中的 pi 相互作用、疏水效应和氢键竞争，并评估传统方法在这些相互作用平衡上的偏差。
**主要结论：** 主要结论是：该 CCSD(T) 质量的 MLIP 能在体相环境中复现耦合簇能量和力，并揭示常用方法会错误描述亲水/疏水平衡，从而扭曲芳香分子与水环境的相互作用。

### 2. Transferable Implicit Solvent Machine Learning Potential for Drugs and Proteins Approaching Ab Initio Accuracy

- Source: arXiv
- Date: 2026-07-12T19:29:24Z
- Venue: physics.chem-ph, cs.LG, q-bio.BM
- Authors: Jan Eckwert, Julija Zavadlav
- Link: https://arxiv.org/abs/2607.10887v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**文章摘要：** 该论文面向生物分子体系中的机器学习原子间势。作者指出，MLP 有望替代 DFT 进行原子尺度建模，但推理速度仍明显慢于经典力场，限制了药物和蛋白质等体系在微秒及更长时间尺度上的应用。
**讨论重点：** 讨论重点是 Transferable Water Implicit Network (TWIN)：一种完全由等变图神经网络参数化的隐式水机器学习势，训练数据来自从头算和实验标签。
**主要结论：** 主要结论是：TWIN 在药物样分子、多肽和蛋白质之间表现出良好可迁移性，在从头算、晶体学和 NMR 基准中取得优异结果，并稳定优于已有机器学习隐式溶剂或粗粒化模型。

### 3. Edge Cluster Expansion with Radial Rotary Attention for Interatomic Potentials

- Source: arXiv
- Date: 2026-07-12T09:17:57Z
- Venue: stat.ML, cond-mat.mtrl-sci, cs.LG
- Authors: Zemin Xu, Wenbo Xie, P. Hu
- Link: https://arxiv.org/abs/2607.10664v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**文章摘要：** 该论文系统研究 SO(2) 理论在机器学习原子间势中的应用，并指出传统 SO(2) 线性架构相对 SO(3) Clebsch-Gordan 张量积存在局限。基于这些分析，作者提出 Wigner D 矩阵的直接笛卡尔构造和递归 Clebsch-Gordan 构造，并引入两个新的交互模块。
**讨论重点：** 讨论重点是如何改进等变原子间势的角向表示能力，尤其是用径向旋转注意力和边簇展开提高模型在材料模拟中的表达能力。
**主要结论：** 主要结论是：作者提出的 TECE-OAM-RRA-1.0 在 OMat24、sAlex 和 MPTrj 等数据上训练后，在 Matbench Discovery 基准中达到当前领先性能。

### 4. Are Machine Learning Interatomic Potentials Truly Practical? A Benchmark of 23 Mainstream Models

- Source: arXiv
- Date: 2026-07-08T17:04:42Z
- Venue: cond-mat.mtrl-sci, cs.CE, physics.comp-ph
- Authors: Hanwen Kang, Tenglong Lu, Sheng Meng, Miao Liu
- Link: https://arxiv.org/abs/2607.07647v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**文章摘要：** 该论文质疑现有 MLIP 基准过度关注静态精度，而忽略推理效率和硬件可扩展性的问题。作者在低成本 NVIDIA DGX Spark 平台上，用统一 ASE 流程和固定 192 原子体系评测 23 个主流开源 MLIP。
**讨论重点：** 讨论重点是机器学习原子间势的实际可用性，包括精度、吞吐量、内存占用和普通实验室硬件上的部署表现。
**主要结论：** 主要结论是：高精度大模型相对轻量模型只带来约 3-5 meV/atom 的精度收益，却牺牲几个数量级的计算吞吐；最差情况下，其速度仅略快于 DFT。

### 5. MLIP Studio: An Open Platform for Interactive Benchmarking and Atomistic Simulations Using Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-08T16:23:57Z
- Venue: cond-mat.mtrl-sci
- Authors: Manas Sharma, Sudeep Punnathanam, Ananth Govind Rajan
- Link: https://arxiv.org/abs/2607.07606v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**文章摘要：** 该论文介绍 MLIP Studio，一个面向分子和材料的开放交互平台。作者指出，通用机器学习原子间势正在改变原子模拟，但实际使用仍受软件生态碎片化、依赖冲突和缺少易用基准工具限制。
**讨论重点：** 讨论重点是把 60 多种通用 MLIP 统一到一个可交互平台中，用于模型测试、结构优化、基准比较和原子尺度模拟。
**主要结论：** 主要结论是：MLIP Studio 降低了 MLIP 使用门槛，并显示基于 MLIP 的预优化可将后续 DFT 优化工作量降低约 33 倍。

### 6. Active rejection enables reliable generalization of universal machine-learning interatomic potentials

- Source: arXiv
- Date: 2026-07-10T14:24:47Z
- Venue: cs.LG
- Authors: Mingxiang Luo, Xinnan Mao, Lu Wang, Lei Bai, Feng Ding, Yuqiang Li
- Link: https://arxiv.org/abs/2607.09456v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**文章摘要：** 该论文关注通用机器学习原子间势的可靠泛化。作者指出，uMLIP 能连接量子力学精度和大尺度分子动力学，但高精度数据成本高，且平均基准表现并不保证每个结构上的能量和力预测都可靠。
**讨论重点：** 讨论重点是 Adaptive Multi-Teacher Routing (ATR)，即把高保真数据构建转化为带不确定性的逐结构决策问题，并主动拒绝不可靠预测。
**主要结论：** 主要结论是：ATR 提高了多个材料体系在有限温度分子动力学中的动力学稳健性，在基线模拟会发生结构坍塌的情形下仍能保持稳定轨迹。

### 7. dpti: An Automated Thermodynamic Integration Workflow for Phase Diagram Calculations with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-06T12:56:52Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Fengbo Yuan, Xin Zhong, Donghao Zheng, Jinzhe Zeng, Linfeng Zhang, Han Wang
- Link: https://arxiv.org/abs/2607.05015v1
- Score: 9.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**文章摘要：** 该论文介绍 dpti，一个用于相图计算的自动化热力学积分工作流。作者指出，热力学积分常用于自由能和相图计算，但由 MLIP 驱动时需要精心设计可逆积分路径，并为每个相和状态点执行大量相关 MD 任务。
**讨论重点：** 讨论重点是如何把机器学习原子间势、热力学积分和自动化分子动力学任务组织成可复用流程，以降低相图计算的人为操作成本。
**主要结论：** 主要结论是：dpti 已通过两个 Deep Potential 示例验证，包括二氧化硅相图和冰 Ih-液态水相边界，能够作为基于 MLIP 的材料相图自动计算工具。

### 8. Dyna-Mat: End-to-end benchmarking of foundation machine learning interatomic potentials in finite-temperature ensembles

- Source: arXiv
- Date: 2026-07-03T15:46:15Z
- Venue: cond-mat.mtrl-sci, physics.chem-ph
- Authors: Mikołaj J. Gawkowski, Nongnuch Artrith, Silvia Bonfanti, Abhijeet Sadashiv Gangan, Hendrik H. Heenen, Joseph Kioseoglou
- Link: https://arxiv.org/abs/2607.03433v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**文章摘要：** 该论文提出 Dyna-Mat-v1.0，用于在有限温度系综中端到端评测基础机器学习原子间势。作者指出，MLIP 正被用作第一性原理计算替代物，但在真实有限温度条件下对结构和动力学可观测量的精度仍缺少系统验证。
**讨论重点：** 讨论重点是用凝聚相第一性原理分子动力学轨迹构建基准，评估基础 MLIP 在实际热力学系综中的结构、动力学和有限温度表现。
**主要结论：** 主要结论是：平均来看，单点力误差较低的模型也会给出较低的结构和动力学可观测量误差，但有限温度基准仍是判断模型可靠性的必要环节。

### 9. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-02T17:57:31Z
- Venue: cs.LG, cs.AI, physics.chem-ph
- Authors: Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, Laura Zichi, Chuin Wei Tan, Marc L. Descoteaux
- Link: https://arxiv.org/abs/2607.02499v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**文章摘要：** 该论文研究 MLIP 训练中的优化器选择。作者指出，虽然模型结构和数据集不断改进，但社区通常默认使用 Adam 或其变体，优化器本身对训练效率和标签利用率的影响长期被忽视。
**讨论重点：** 讨论重点是 SOAP 和 Muon 等优化器是否能在 MLIP 训练中提高收敛速度、最终精度和标签效率。
**主要结论：** 主要结论是：这些优化器在收敛速度和最终精度上都能显著优于 Adam，说明优化器选择是 MLIP 设计中被低估但影响很大的因素。

### 10. Enerzyme: A Framework for Efficient Training of Reactive Neural Network Potentials for Enzyme Catalysis with Application to Methyltransferases

- Source: arXiv
- Date: 2026-07-01T18:24:10Z
- Venue: physics.chem-ph, cs.LG, q-bio.BM
- Authors: Weiliang Luo, Heather J. Kulik
- Link: https://arxiv.org/abs/2607.01362v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**文章摘要：** 该论文提出 Enerzyme，用于高效训练酶催化反应的反应性神经网络势。作者指出，量子力学簇模型适合研究酶反应机理但计算昂贵，而酶体系的大尺寸、隐式溶剂、极化和电荷转移又给 NNP 带来额外挑战。
**讨论重点：** 讨论重点是如何为甲基转移酶等酶催化体系构建可靠的反应性神经网络势，并处理大体系、极化和反应路径采样等问题。
**主要结论：** 主要结论是：迭代柔性扫描和 nudged elastic band 计算对 NNP 的要求比常规数据集指标更严格，因此反应性酶体系需要更面向机理任务的训练和验证框架。

## 凝聚态物理强关联体系和多铁性质

### 1. Strain-Tunable Shift Current and Magneto-Optical Kerr Effect in Multiferroic Altermagnet Fe2Mo3O8

- Source: arXiv
- Date: 2026-07-14T14:14:24Z
- Venue: cond-mat.mtrl-sci
- Authors: Shengqiao Wang, Bo Zhao, Harish K. Singh, Jiahao Xie, Fu Li, Hongbin Zhang
- Link: https://arxiv.org/abs/2607.12799v1
- Score: 17.0
- Match: 标题匹配 multiferroic; 最近 3 天发布

**文章摘要：** 该研究关注多铁交替磁体 Fe2Mo3O8 中的应变可调移位电流和磁光 Kerr 效应。作者指出，交替磁性结合了铁磁体的可调性和反铁磁体的优点，而极性多铁 Fe2Mo3O8 为研究铁电极化、交替磁序和自旋相关响应的耦合提供了理想平台。
**讨论重点：** 讨论重点是利用第一性原理计算系统研究 Fe2Mo3O8 中极化、自旋劈裂、移位电流和磁光响应之间的耦合关系，以及应变对这些响应的调控。
**主要结论：** 主要结论是：翻转铁电极化不仅会反转移位电流符号，还会显著重塑动量空间中的自旋劈裂纹理。

### 2. Magnetic field-driven phase switching in the antiferromagnetic Mott insulator Ca$_3$(Ru$_{0.99}$Ti$_{0.01}$)$_2$O$_7$

- Source: arXiv
- Date: 2026-07-14T13:09:26Z
- Venue: cond-mat.str-el
- Authors: Ksenia S. Rabinovich, Tim Priessnitz, Nils Gross, George Jackeli, Maximilian J. Krautloher, Pascal Reiss
- Link: https://arxiv.org/abs/2607.12737v1
- Score: 17.0
- Match: 标题匹配 Mott insulator; 最近 3 天发布

**文章摘要：** 该论文研究 Ti 稀释替代 Ca3Ru2O7 后形成的带宽控制反铁磁 Mott 绝缘相。作者指出，即使只有 1% Ti 替代，Mott 绝缘基态仍与母体 Ca3Ru2O7 的基态接近简并，后者在金属 RuO2 双层内呈铁磁排列、层间反铁磁堆垛。
**讨论重点：** 讨论重点是 Ca3(Ru0.99Ti0.01)2O7 中磁场诱导相切换及其 H-T 相图，用以理解 Mott 绝缘、反铁磁性和电子-晶格耦合之间的自由能竞争。
**主要结论：** 主要结论是：尽管电子动能和电子-晶格耦合参与自由能平衡，该体系的 H-T 相图仍异常简单，接近典型各向异性反铁磁体，但临界场被显著重整化。

### 3. Halogen control of magnetic competition in Kitaev candidate Ru$X_3$ ($X =$ Cl, Br)

- Source: arXiv
- Date: 2026-07-14T10:13:10Z
- Venue: cond-mat.str-el
- Authors: Ryuta Iwazaki, Shinnosuke Koyama, Takashi Koretsune, Shintaro Hoshino, Joji Nasu
- Link: https://arxiv.org/abs/2607.12595v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 Mott insulator; 最近 3 天发布

**文章摘要：** 该论文研究 Kitaev 自旋液体候选材料 RuX3 (X=Cl, Br) 中卤素对磁性竞争的调控。作者从第一性原理得到的多轨道 Hubbard 模型出发，构建有效赝自旋模型，并比较 RuCl3 和 RuBr3 的磁态。
**讨论重点：** 讨论重点是卤素替换如何改变 Wannier 轨道范围、层间交换和多轨道 Hubbard 模型中的磁性竞争，从而影响 Kitaev 候选体系的有效自旋相互作用。
**主要结论：** 主要结论是：RuBr3 相比 RuCl3 具有更扩展的 Wannier 轨道和更强的层间交换相互作用，这会显著改变其磁性竞争格局。

### 4. Electric field controlled spin transport in a topological insulator interfaced with a ferroelectric antiferromagnet

- Source: arXiv
- Date: 2026-07-15T16:58:29Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Yogesh Kumar, Pushpendra Gupta, Xinyan Li, Richa Mudgal, Ashish Omar, Ryan Chen
- Link: https://arxiv.org/abs/2607.14031v1
- Score: 14.0
- Match: 摘要匹配 multiferroic; 最近 3 天发布

**文章摘要：** 该论文研究拓扑绝缘体 Bi2Te3 与反铁磁多铁 BiFeO3 界面中的电场控制自旋输运。作者指出，拓扑绝缘体的自旋-电荷转换常通过磁性界面研究，但无外磁场条件下的真实响应仍需澄清。
**讨论重点：** 讨论重点是利用非局域自旋输运器件直接验证 Bi2Te3/BiFeO3 界面的自旋-电荷转换，并探索铁电反铁磁体对拓扑表面态自旋输运的电场调控。
**主要结论：** 主要结论是：Bi2Te3 和 BiFeO3 界面自旋输运的厚度依赖显示出拓扑表面态主导的特征，为低能耗自旋器件提供了可行路径。

### 5. Stoner transitions beyond mean-field in two-dimensional electronic systems: a diagrammatic Monte Carlo study

- Source: arXiv
- Date: 2026-07-15T10:15:14Z
- Venue: cond-mat.str-el
- Authors: Yueh-Chen Lee, Nikolay P. Prokof'ev, Andrey V. Chubukov
- Link: https://arxiv.org/abs/2607.13675v1
- Score: 14.0
- Match: 摘要匹配 ferromagnetism; 最近 3 天发布

**文章摘要：** 该论文研究二维电子体系中超越平均场近似的 Stoner 转变。作者指出，排斥相互作用费米子的 Stoner 不稳定性通常在平均场或 ladder 近似中研究，而本文考虑单谷和双谷二维电子体系中更高阶关联效应的影响。
**讨论重点：** 讨论重点是用图解 Monte Carlo 方法分析二维电子体系中的铁磁 Stoner 转变，并比较平均场以外涨落和相互作用动量截断的作用。
**主要结论：** 主要结论是：在单谷体系中，只有当相互作用携带的动量转移存在截断时，低密度下才会发生通向铁磁性的 Stoner 转变。

### 6. The Sample Pre-selection and Characterization Station at the SECUF: Instrumentation, Capabilities, and Representative Scientific Achievements

- Source: arXiv
- Date: 2026-07-15T01:48:48Z
- Venue: cond-mat.str-el
- Authors: Xu Chen, Tao Sun, Huifen Ren, Minjie Cui, Jun Luo, Shuai Zhang
- Link: https://arxiv.org/abs/2607.13375v1
- Score: 13.0
- Match: 摘要匹配 high-temperature superconductivity; 最近 3 天发布

**文章摘要：** 该论文介绍 SECUF 的样品预筛选与表征站。SECUF 是面向凝聚态物理和材料科学前沿研究的极端条件综合用户设施，可提供超高压、超低温、强磁场和超快光场等条件。
**讨论重点：** 讨论重点是 F2 样品预筛选与表征站的仪器能力、代表性应用，以及其在高温超导和极端条件物性研究中的支撑作用。
**主要结论：** 主要结论是：该站点正在通过集成高压池和自建辅助测量系统等技术发展扩展能力，为复杂材料的极端条件筛选和表征提供平台。

### 7. Precision quantum simulation of magnon spectra and interactions

- Source: arXiv
- Date: 2026-07-14T22:11:22Z
- Venue: quant-ph, cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Trond I. Andersen, Nikita Astrakhantsev, Jeronimo Martinez, Will Morong, Johannes Motruk, Dario Rossi
- Link: https://arxiv.org/abs/2607.13301v1
- Score: 13.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**文章摘要：** 该论文研究磁振子谱和相互作用的精密量子模拟。作者指出，量子模拟有望推进材料发现，但解析复杂物质态中的相互作用动力学需要同时实现高保真演化和对单个准粒子的精细操控。
**讨论重点：** 讨论重点是通过非线性测量、self-scattering 机制研究和 pump-probe 光谱，直接表征量子多体体系中的磁振子相互作用。
**主要结论：** 主要结论是：磁振子衰减率在布里渊区内存在显著变化，在 van Hove 奇点附近增强，而在边缘局域模式中受到抑制。

### 8. Theoretical prediction of structural stability and superconductivity in T-hexagonal molybdenum dihydrides Monolayer

- Source: arXiv
- Date: 2026-07-14T22:08:40Z
- Venue: cond-mat.supr-con
- Authors: Jakkapat Seeyangnok, Udomsilp Pinsook
- Link: https://arxiv.org/abs/2607.13297v1
- Score: 13.0
- Match: 摘要匹配 high-temperature superconductivity; 最近 3 天发布

**文章摘要：** 该论文从理论上预测 T-六角相二氢化钼单层的结构稳定性和超导性。作者指出，常压高温超导氢富材料仍是凝聚态物理的重要目标，而二维过渡金属氢化物可能绕开体相氢化物对极端压力的需求。
**讨论重点：** 讨论重点是利用第一性原理计算研究 MoH2 单层的结构稳定性、电子性质和声子介导超导，并评估其作为二维氢化物超导候选体系的可行性。
**主要结论：** 主要结论是：总能计算显示八面体 T 相比此前报道的三角棱柱 H 相低 0.198 eV，因此 T 相才是真正的基态构型。

### 9. Reproducible Reservoir Computing with Thermally Driven Superparamagnets: Controlling Temperature Sensitivity

- Source: arXiv
- Date: 2026-07-14T14:57:12Z
- Venue: cs.ET, cond-mat.mes-hall, cs.AI
- Authors: Zhengfei Chen, Alex Welbourne, Matthew O. A. Ellis, Dan A. Allwood, Eleni Vasilaki, Thomas J. Hayward
- Link: https://arxiv.org/abs/2607.12840v1
- Score: 13.0
- Match: 摘要匹配 magnetoelectric coupling; 最近 3 天发布

**文章摘要：** 该论文研究热驱动超顺磁体用于可复现 reservoir computing 的温度敏感性控制。作者指出，非传统计算系统若要实际部署，必须在真实环境条件下保持稳健性能；应变诱导磁电耦合驱动的超顺磁纳米点阵列是低能耗计算基底的候选体系。
**讨论重点：** 讨论重点是通过引入优化的异质性来稳定 reservoir 在不同环境温度下的表现，并分析磁电耦合超顺磁体系作为计算硬件的可控性。
**主要结论：** 主要结论是：在 NARMA-10 任务上，优化异质性可在 5-35 摄氏度范围内稳定 reservoir 性能，同时几乎不损失最佳性能。

### 10. Giant magnetocaloric effect at low fields in triangular-lattice NdMgAl$_{11}$O$_{19}$

- Source: arXiv
- Date: 2026-07-14T02:03:04Z
- Venue: cond-mat.str-el
- Authors: Yantao Cao, He Sun, Zhendong Fu, Zhaoming Tian, Huiqian Luo, Junsen Xiang
- Link: https://arxiv.org/abs/2607.12262v1
- Score: 12.0
- Match: 摘要匹配 quantum spin liquid; 最近 3 天发布

**文章摘要：** 该论文研究三角晶格 NdMgAl11O19 在低磁场下的巨磁热效应。作者指出，亚开尔文磁制冷需要材料在低温下通过抑制磁有序保持较大磁熵，而量子自旋液体因保留强量子涨落，是高性能磁制冷材料的潜在平台。
**讨论重点：** 讨论重点是几何阻挫、强自旋-轨道耦合和晶体场效应如何共同提升稀土磁体的低温磁热响应，并将量子自旋液体思想用于低温磁制冷设计。
**主要结论：** 主要结论是：比热测量显示该体系在 50 mK 以下仍保留大量磁熵，说明其在低场亚开尔文磁制冷方面具有潜力。
