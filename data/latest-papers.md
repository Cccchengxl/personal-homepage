# Latest papers for 程旭丽

Updated: 2026-08-11T04:57:38.894261+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 14.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries

- Source: arXiv
- Date: 2026-08-07T07:36:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Timothée Jamin, Zhencai Li, Kasper Tolborg, Yuanzheng Yue
- Link: https://arxiv.org/abs/2608.06902v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 全固态锂电池需要将快速室温离子传输与机械鲁棒性和界面兼容性相结合的固体电解质。沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 这是通过使用机器学习原子间势来模拟晶体和玻璃态 ZIF-4 和 ZIF-62 中的 Li+ 传输来实现的。结构紊乱将 Li+ 迁移的活化能从约 0.35 eV 降低至 0.16 eV，并将 ZIF-4 的外推室温扩散系数增加了一个数量级以上，而 ZIF-62 则增加了近七倍。 非高斯动力学和范霍夫相关函数的分析表明，Li+在晶体ZIF中的扩散是通过明确的笼子之间罕见的、动态异质的跳跃事件发生的，而玻璃态ZIF中的Li+扩散更加均匀、连续和类似Fickian，受益于广泛分布的配位几何形状和迁移势垒。晶体 ZIF 中的 Li+ 扩散具有强烈的各向异性，这反映出咪唑盐和苯并咪唑盐环的有序取向沿不同的晶体方向施加了不同的能垒。 玻璃化后，这些环的方向变得随机，因此，Li + 的扩散变得各向同性或近各向同性。这些发现表明，精心设计的金属有机框架玻璃是高性能固态电解质的有希望的候选者。
**讨论重点：** 沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Local Structure Dictates Ionic Transport and Mechanical Properties in Glassy Solid Electrolytes for Lithium Batteries

- Source: arXiv
- Date: 2026-08-07T07:29:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Rasmus Christensen, Timothée Jamin, Zhencai Li, Qi Zhang
- Link: https://arxiv.org/abs/2608.06895v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 由硫化物和卤化物玻璃组成的电解质由于其可加工性、缺乏晶界和相对较高的离子电导率而成为全固态锂电池的有希望的候选者。然而，它们的离子电导率和机械性能仍然不能满足实际应用。固体电解质的重大进步需要对其微观结构的透彻了解。 在这里，我们通过采用基于机器学习原子间势的分子动力学模拟，揭示了一系列玻璃态固体电解质的结构、离子传输特性和机械稳定性之间的联系。具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。将 P2S5 引入 B2S3 基玻璃中会引发关键的结构转变，从而增强离子电导率和机械纳米延展性。 对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。同时，灵活的 P-S-P 配置可以通过键弯曲实现能量耗散，从而实现脆性到延性的转变。然而，过量的 P2S5 会增加多磷酸盐（例如 P2S6 和 P2S7）的比例，从而聚合结构网络并最终阻碍 Li+ 的迁移率。 因此，我们的工作为工程玻璃电解质提供了原子原理，具有平衡的离子电导率和机械鲁棒性。
**讨论重点：** 具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. An Exchange-Correlation Functional for Fast and Accurate Modeling of Ferroelectric Perovskites

- Source: arXiv
- Date: 2026-08-05T13:12:10Z
- Venue: cond-mat.mtrl-sci
- Authors: Owain T. Beynon, Chiara Gattinoni
- Link: https://arxiv.org/abs/2608.04806v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 我们提出了一种新颖的交换关联泛函 C09x-PBEc，它将 C09 交换与 PBE 关联相结合，可以准确地模拟钙钛矿的铁电特性，同时保留 GGA 泛函的计算效率。随着人们对开发机器学习原子间势 (MLIP) 来模拟具有技术相关性的大规模铁电系统的兴趣日益浓厚，仔细研究用于计算 MLIP 训练的力、能量和应力的密度泛函理论交换相关函数非常重要。 以典型铁电体钛酸铅、PbTiO3 和钛酸钡、BaTiO3 为例，我们表明许多广泛使用的泛函往往会高估其晶格常数和自发极化。相反，与实验相比，具有 C09 交换的非局域范德华函数可以准确地捕获这些属性，但计算开销比 GGA 等更大。 我们证明，C09x-PBEc 将 C09 交换提供的精度与 GGA 的计算承受能力相结合，使其成为用于铁电钙钛矿 MLIP 训练的绝佳候选者。我们还证明，使用 C09x-PBEc 训练的 MLIP 在实验中准确再现了 PbTiO3 的铁电到顺电相变温度，表明使用 GGA 训练的 MLIP 有了显着的改进。
**讨论重点：** 我们提出了一种新颖的交换关联泛函 C09x-PBEc，它将 C09 交换与 PBE 关联相结合，可以准确地模拟钙钛矿的铁电特性，同时保留 GGA 泛函的计算效率。随着人们对开发机器学习原子间势 (MLIP) 来模拟具有技术相关性的大规模铁电系统的兴趣日益浓厚，仔细研究用于计算 MLIP 训练的力、能量和应力的密度泛函理论交换相关函数非常重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 5. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议，在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 6. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 7. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 10. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

## 凝聚态物理强关联体系和多铁性质

### 1. Microscopic Origin of Spin Splitting in Altermagnetic CrSb Thin Films

- Source: arXiv
- Date: 2026-08-09T14:37:26Z
- Venue: cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Dai Mingyang, Song Hongquan, Kang Zhuo, Xu Yuanji, Tian Fuyang
- Link: https://arxiv.org/abs/2608.08741v1
- Score: 30.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials

**中文摘要：** 由于其依赖于动量的自旋分裂，交变磁体最近成为自旋电子应用中有前途的材料。其中，金属CrSb因其巨大的自旋分裂和高尼尔温度而特别引人注目。然而，块状和薄膜 CrSb 中独特的自旋分裂行为的微观起源仍未解决。在这里，我们使用第一性原理计算系统地研究了具有不同表面取向的 CrSb 板的电子结构。 尽管所有考虑的板片都保留了与交变磁性兼容的自旋群对称性，但它们表现出明显不同的电子结构：(2$\bar{1}\bar{1}$0)板片保留了明显的交变磁自旋分裂，而(0001)和(10$\bar{1}$0)板片显示出近自旋简并的能带。我们证明，降维从根本上改变了交变磁自旋分裂的微观起源。 与块状 CrSb 不同，薄膜中的交变磁自旋分裂需要长程晶胞间共面 Cr-Sb 跳跃，而 Sb-Sb 跳跃提供额外的贡献。这些跳跃路径的保留或抑制解释了自旋分裂的强烈表面依赖性。我们的研究结果建立了一种理解降维交变磁性的微观机制，并为低维交变磁性材料中的工程自旋分裂提供了一般原理。
**讨论重点：** 在这里，我们使用第一性原理计算系统地研究了具有不同表面取向的 CrSb 板的电子结构。其中，金属CrSb因其巨大的自旋分裂和高尼尔温度而特别引人注目。 结合关键词看，阅读时应重点关注交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Time-Reversal-Invariant Altermagnetic Acoustic Crystals

- Source: arXiv
- Date: 2026-08-09T17:20:24Z
- Venue: cond-mat.mes-hall
- Authors: Tianzhi Xia, Han-Rong Xia, Jinglin Liu, Xiying Fan, Zebin Zhu, Zhen Gao
- Link: https://arxiv.org/abs/2608.08827v1
- Score: 27.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交替磁体已成为一类新型磁性材料，它将自旋分裂电子​​带与零净磁化强度结合在一起。然而，将这种范式扩展到经典波系统从根本上来说是具有挑战性的，因为传统的实现需要打破时间反转对称性（TRS）。在这里，我们通过引入两个赝自旋自由度并构建一个赝时间反转算子来克服这一限制，该算子忠实地再现其物理对应物的动作，同时保留实际的 TRS。 在此框架的基础上，我们从理论上提出并通过实验实现了第一个时间反转不变的交变磁声晶体。声学测量直接揭示了在严格保留 TRS 的条件下赝自旋相关的能带分裂——交变磁力的一个定义标志。此外，交变磁声晶体表现出亚晶格赝自旋锁定，能够灵活控制声学赝自旋分裂和滤波。 我们的工作将声学晶体建立为探索交磁物理的多功能平台，并为非磁性设备中自旋激发的波操纵开辟了新途径。
**讨论重点：** 在此框架的基础上，我们从理论上提出并通过实验实现了第一个时间反转不变的交变磁声晶体。然而，将这种范式扩展到经典波系统从根本上来说是具有挑战性的，因为传统的实现需要打破时间反转对称性（TRS）。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Magnetotransport evolution and nonlinear Hall effect in altermagnetic MnTe

- Source: arXiv
- Date: 2026-08-10T09:49:13Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn, cond-mat.str-el
- Authors: Wei Zhou, Zhifeng Xue, Yunxing Li, Nannan Tang, Ye Tao, Dingyong Zhong
- Link: https://arxiv.org/abs/2608.09371v1
- Score: 25.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 六方锰碲是一种典型的半导体交变磁体，其特性受到内在无序的严重影响，但由此产生的不同输运机制如何塑造其磁输运行为以及相对论自旋轨道耦合（SOC）的作用仍有待澄清。在这里，我们对 MnTe 块状单晶中的各向异性磁阻 (AMR)、平面霍尔效应 (PHE) 和非线性输运进行了系统研究。 在尼尔温度 (TN ~ 304 K) 以下，高温金属状态下 AMR 和 PHE 中高阶谐波的出现揭示了磁序、晶体对称性和 SOC 的相互作用。在相对较低的温度下，高阶对称性的消失与传输交叉进入跳跃传导状态同时发生，这表明载流子局域化降低了对费米表面拓扑的传输敏感性。 此外，我们还检测到了独特的二阶非线性霍尔信号，为互磁 MnTe 中的宏观反演不对称响应提供了证据。将研究扩展到局部区域，为了解无序和 SOC 在宏观电荷传输中的微妙作用提供了重要见解。因此，我们的工作强调了探索跨不同传导机制的磁输运以全面了解交磁特性的必要性。
**讨论重点：** 在这里，我们对 MnTe 块状单晶中的各向异性磁阻 (AMR)、平面霍尔效应 (PHE) 和非线性输运进行了系统研究。在尼尔温度 (TN ~ 304 K) 以下，高温金属状态下 AMR 和 PHE 中高阶谐波的出现揭示了磁序、晶体对称性和 SOC 的相互作用。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Altermagnetism-Induced Spin-resolved electronic structure in Janus FeX0.5Y0.5 Monolayers (X, Y = S, Se, Te)

- Source: arXiv
- Date: 2026-08-10T03:00:42Z
- Venue: cond-mat.mtrl-sci
- Authors: Mengyang Zhang, Jie Li, Yifei Chen, Shifang Li, Zhentao Fu, Jianxin Zhong
- Link: https://arxiv.org/abs/2608.09054v1
- Score: 24.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 实现超导材料中的自旋分辨电子特性是一个关键前沿，它为无耗散自旋器件提供了新颖的基础物理和潜力。在这里，我们通过使用近藤型模型和第一性原理计算预测了一系列源自铁基超导体（例如 FeSe、FeTe 和 FeS）的 Janus FeX0.5Y0.5 单层。这些 Janus 结构表现出显着的自旋分裂电子​​态、大的拓扑带隙 (51.4 meV) 和高尼尔温度 (415 K)。 我们进一步揭示，可以通过施加面内应变来有效地调节谷极化，并且可以通过改变费米能级来操纵由此产生的谷极化反常霍尔电导率。我们的工作提出了一种基于交变磁性的新策略，用于在超导系统中设计自旋分裂态，并激发了对超导自旋电子学的进一步探索。
**讨论重点：** 在这里，我们通过使用近藤型模型和第一性原理计算预测了一系列源自铁基超导体（例如 FeSe、FeTe 和 FeS）的 Janus FeX0.5Y0.5 单层。这些 Janus 结构表现出显着的自旋分裂电子​​态、大的拓扑带隙 (51.4 meV) 和高尼尔温度 (415 K)。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Type-II Mirror Chern Insulator in Altermagnets

- Source: arXiv
- Date: 2026-08-07T16:16:42Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Amrita Mukherjee, Pritesh Srivastava, Rahul Verma, Bahadur Singh
- Link: https://arxiv.org/abs/2608.07374v1
- Score: 21.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 尽管净磁化强度为零，但具有动量相关自旋分裂的交变磁体可以在打破时间反转对称性的情况下支持独特的拓扑状态。我们预测二维交替磁体中具有动量分离边缘模式的镜像对称保护的拓扑晶体绝缘体。使用方八边形晶格模型，我们证明交变磁序生成对称相关的谷极化狄拉克节点，这些节点通过自旋轨道耦合产生间隙，产生$C_{\mathcal{M}}=2$的镜陈绝缘体。 传统的镜陈绝缘体中，两个镜面保护的边缘模式以相同的动量交叉形成狄拉克锥，与此相反，交变磁自旋分裂和谷选择性能带反转将这些边缘模式的动量分开。我们将此相称为 II 型镜陈绝缘体。我们进一步提出 PbSe/$\mathrm{V_2Se_2O}$ 异质双层作为通过交变邻近效应实现该相的候选材料。我们的结果确立了交变磁学是通向具有动量分离边缘模式的镜面保护拓扑相的途径。
**讨论重点：** 我们进一步提出 PbSe/$\mathrm{V_2Se_2O}$ 异质双层作为通过交变邻近效应实现该相的候选材料。使用方八边形晶格模型，我们证明交变磁序生成对称相关的谷极化狄拉克节点，这些节点通过自旋轨道耦合产生间隙，产生$C_{\mathcal{M}}=2$的镜陈绝缘体。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Ferroelectric-controllable spin-orbit torque in two-dimensional multiferroic heterostructure

- Source: arXiv
- Date: 2026-08-07T19:50:56Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Weiyi Pan, Gusthavo M. S. Brizolla, Jaroslav Fabian
- Link: https://arxiv.org/abs/2608.07731v1
- Score: 18.0
- Match: 标题匹配 multiferroic; 摘要匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 自旋轨道扭矩（SOT）能够实现磁化的电控制，在下一代自旋电子器件的开发中发挥着至关重要的作用。在二维范德华系统中实现 SOT，并通过铁电性实现高效的非易失性操作，对于实现具有增强存储密度的可调谐逻辑器件将非常有益。 在这项工作中，基于第一性原理计算，并使用多铁性 Fe$_{3}$GeTe$_{2}$/In$_{2}$Se$_{3}$ 异质结构作为代表性示例，我们证明，切换 In$_{2}$Se$_{3}$ 层的铁电极化会导致异质结构内磁化相关的扭矩分布发生显着变化。具体来说，当磁化位于扭矩最大的平面时，将 In$_{2}$Se$_{3}$ 的极化从上到下反转，可将总扭矩提高到其原始值的 150% 以上。 这种巨大的变化主要源于时间反转奇数扭矩的 $z$ 分量的极化引起的调制，这主要与 Fe$_{3}$GeTe$_{2}$ 层中的中间 Fe 层贡献的原子分辨扭矩约 233% 的变化有关。进一步的分析表明，费米表面上 $Γ$ 附近的电子态在极化切换时经历了显着的重构，这是观察到的时间反转奇扭矩变化的原因。 我们的研究结果不仅为范德华多铁异质结构的功能潜力提供了新的见解，而且还为实现电可调SOT提供了可行的策略，为未来的可编程自旋电子器件铺平了道路。
**讨论重点：** 自旋轨道扭矩（SOT）能够实现磁化的电控制，在下一代自旋电子器件的开发中发挥着至关重要的作用。在二维范德华系统中实现 SOT，并通过铁电性实现高效的非易失性操作，对于实现具有增强存储密度的可调谐逻辑器件将非常有益。 结合关键词看，阅读时应重点关注多铁性、铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 7. Defect-Controlled Multiferroicity via Stacking Control in Nonmagnetic van der Waals Bilayers

- Source: arXiv
- Date: 2026-08-07T18:00:05Z
- Venue: cond-mat.mtrl-sci
- Authors: Bumseop Kim, Sayed Ali Akbar Ghorashi, Andrew M. Rappe
- Link: https://arxiv.org/abs/2608.07666v1
- Score: 18.0
- Match: 标题匹配 multiferroic; 摘要匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 我们提出了一种通用范例，将空位局域磁性直接耦合到非磁性范德华（vdW）双层中的界面滑动铁电性。利用双层六方氮化硼（hBN）作为典型的 vdWs 宿主系统，我们使用第一原理计算来表明单个空位充当局部配准传感器，通过以缺陷为中心的偏振偏移来提升极性滑动伙伴之间的简并性。 对于层间空位对，我们发现了缺陷选择性，其中主子晶格完全决定了层间交换，从而稳定了亚铁磁或反铁磁配置。应用面外电场选择极配准并驱动补偿的尼尔阶参数的幅度调制。这些发现通过跨多种非磁性二维异质结构的堆叠控制建立了稳健的、依赖于亚晶格的多铁性功能工程。
**讨论重点：** 我们提出了一种通用范例，将空位局域磁性直接耦合到非磁性范德华（vdW）双层中的界面滑动铁电性。利用双层六方氮化硼（hBN）作为典型的 vdWs 宿主系统，我们使用第一原理计算来表明单个空位充当局部配准传感器，通过以缺陷为中心的偏振偏移来提升极性滑动伙伴之间的简并性。 结合关键词看，阅读时应重点关注多铁性、铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. A spin-bond theory unifying non-relativistic spin splitting and emergent spin-orbit textures

- Source: arXiv
- Date: 2026-08-10T14:22:59Z
- Venue: cond-mat.mtrl-sci
- Authors: S. Allende, R. M. Otxoa
- Link: https://arxiv.org/abs/2608.09644v1
- Score: 17.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 净磁化强度消失的磁序可以产生非相对论性自旋分裂带，大致分为偶宇称交替磁体和奇宇称\(p\)波磁体。在这里，我们引入了一种自旋键理论，它将这些看似不同的现象统一到一个代数框架中。我们证明非相对论性自旋纹理从根本上由电子键的两个组成部分控制：酉自旋相位和厄米自旋振幅。 酉扇区产生奇宇称 p 波和涌现的自旋轨道状纹理，而厄米扇区产生偶宇称自旋场，包括均匀的\(\)分裂和键结构的交磁极限。除了统一已知相之外，我们的理论还揭示了当酉扇区和厄米扇区无法交换时出现的混合非交换状态，揭示了潜在的非交换自旋键结构。 这种状态产生了一种非共面的自旋纹理，其特征是动量均匀的横向自旋极化，为自旋和角度分辨的光电子能谱提供了直接的光谱指纹。此外，我们确定这种合成自旋轨道耦合可以通过几何控制键合扇区的非交换来动态调整。通过为这种调谐提供微观基础，我们的理论为包括无场自旋量子位在内的高级应用铺平了道路。
**讨论重点：** 在这里，我们引入了一种自旋键理论，它将这些看似不同的现象统一到一个代数框架中。我们证明非相对论性自旋纹理从根本上由电子键的两个组成部分控制：酉自旋相位和厄米自旋振幅。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Ground-state phase diagram and route to supersolidity in a two-component extended Bose-Hubbard model

- Source: arXiv
- Date: 2026-08-09T14:34:49Z
- Venue: cond-mat.quant-gas, cond-mat.str-el
- Authors: Xuexin Qiu, Ning Bian, Yang Liu, Saisai He, Z. Y. Xie, Hong-Gang Luo
- Link: https://arxiv.org/abs/2608.08738v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 我们使用投影纠缠对态研究了最近用偶极激子实现的双组分扩展 Bose-Hubbard 模型的基态相图。对于实验相关的参数体系，确定了棋盘相、莫特绝缘相、超流体相和真空相。这些相表现出轨道选择性特征，其中两种成分占据不同的量子态，但我们没有发现超固相的证据。 超固体的缺失归因于强相互作用主导的微观能量尺度，这严重限制了超流体状态。在超固体机制的指导下，我们进一步探索了一种具有增强的组分跳跃的附近参数状态，并确定了轨道选择性超固体相。进一步的有限键维和晶胞分析确定了该相的稳健性。我们的结果阐明了偶极激子平台的零温相结构，并为在这种情况下实现超固体提供了可能的途径。
**讨论重点：** 我们使用投影纠缠对态研究了最近用偶极激子实现的双组分扩展 Bose-Hubbard 模型的基态相图。对于实验相关的参数体系，确定了棋盘相、莫特绝缘相、超流体相和真空相。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Fermionic Lattice Supersolidity in the Attractive Three-Color Fermi-Hubbard Model

- Source: arXiv
- Date: 2026-08-08T15:15:04Z
- Venue: cond-mat.str-el, cond-mat.quant-gas
- Authors: Xiang Li, Yu Wang
- Link: https://arxiv.org/abs/2608.08178v1
- Score: 16.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 最近在方形光学晶格上实验实现的半填充三色费米-哈伯德模型为探索传统 SU(2) 系统之外的奇异物质态提供了一个新颖的平台。在这封信中，我们使用行列式量子蒙特卡罗模拟研究了具有颜色相关吸引力相互作用的三色费米-哈伯德模型。我们发现，在量子简并温度下，中等到强相互作用的双色子系统和弱耦合的第三色环境之间的相互作用会产生晶格费米超固态。 这种超固态的特点是电荷密度波和颜色超流体秩序的共存，对于利用当前技术进行实验检测非常有希望。我们的结果表明，方形光学晶格上有吸引力的三色费米-哈伯德模型为探索超冷晶格费米子的超固体性提供了一个实验上可访问的系统，只需要简单的晶格几何形状和易于调节的现场相互作用。
**讨论重点：** 在这封信中，我们使用行列式量子蒙特卡罗模拟研究了具有颜色相关吸引力相互作用的三色费米-哈伯德模型。最近在方形光学晶格上实验实现的半填充三色费米-哈伯德模型为探索传统 SU(2) 系统之外的奇异物质态提供了一个新颖的平台。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
