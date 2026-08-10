# Latest papers for 程旭丽

Updated: 2026-08-10T05:15:21.403824+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 15.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries

- Source: arXiv
- Date: 2026-08-07T07:36:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Timothée Jamin, Zhencai Li, Kasper Tolborg, Yuanzheng Yue
- Link: https://arxiv.org/abs/2608.06902v1
- Score: 12.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 全固态锂电池需要将快速室温离子传输与机械鲁棒性和界面兼容性相结合的固体电解质。沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 这是通过使用机器学习原子间势来模拟晶体和玻璃态 ZIF-4 和 ZIF-62 中的 Li+ 传输来实现的。结构紊乱将 Li+ 迁移的活化能从约 0.35 eV 降低至 0.16 eV，并将 ZIF-4 的外推室温扩散系数增加了一个数量级以上，而 ZIF-62 则增加了近七倍。 非高斯动力学和范霍夫相关函数的分析表明，Li+在晶体ZIF中的扩散是通过明确的笼子之间罕见的、动态异质的跳跃事件发生的，而玻璃态ZIF中的Li+扩散更加均匀、连续和类似Fickian，受益于广泛分布的配位几何形状和迁移势垒。晶体 ZIF 中的 Li+ 扩散具有强烈的各向异性，这反映出咪唑盐和苯并咪唑盐环的有序取向沿不同的晶体方向施加了不同的能垒。 玻璃化后，这些环的方向变得随机，因此，Li + 的扩散变得各向同性或近各向同性。这些发现表明，精心设计的金属有机框架玻璃是高性能固态电解质的有希望的候选者。
**讨论重点：** 沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Local Structure Dictates Ionic Transport and Mechanical Properties in Glassy Solid Electrolytes for Lithium Batteries

- Source: arXiv
- Date: 2026-08-07T07:29:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Rasmus Christensen, Timothée Jamin, Zhencai Li, Qi Zhang
- Link: https://arxiv.org/abs/2608.06895v1
- Score: 12.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 由硫化物和卤化物玻璃组成的电解质由于其可加工性、缺乏晶界和相对较高的离子电导率而成为全固态锂电池的有希望的候选者。然而，它们的离子电导率和机械性能仍然不能满足实际应用。固体电解质的重大进步需要对其微观结构的透彻了解。 在这里，我们通过采用基于机器学习原子间势的分子动力学模拟，揭示了一系列玻璃态固体电解质的结构、离子传输特性和机械稳定性之间的联系。具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。将 P2S5 引入 B2S3 基玻璃中会引发关键的结构转变，从而增强离子电导率和机械纳米延展性。 对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。同时，灵活的 P-S-P 配置可以通过键弯曲实现能量耗散，从而实现脆性到延性的转变。然而，过量的 P2S5 会增加多磷酸盐（例如 P2S6 和 P2S7）的比例，从而聚合结构网络并最终阻碍 Li+ 的迁移率。 因此，我们的工作为工程玻璃电解质提供了原子原理，具有平衡的离子电导率和机械鲁棒性。
**讨论重点：** 具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. An Exchange-Correlation Functional for Fast and Accurate Modeling of Ferroelectric Perovskites

- Source: arXiv
- Date: 2026-08-05T13:12:10Z
- Venue: cond-mat.mtrl-sci
- Authors: Owain T. Beynon, Chiara Gattinoni
- Link: https://arxiv.org/abs/2608.04806v1
- Score: 10.0
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

### 1. Emergent Surface Altermagnetism

- Source: arXiv
- Date: 2026-08-06T02:13:02Z
- Venue: cond-mat.mtrl-sci
- Authors: Yuzhong Hu, Pan Zhou, Baoru Pan, Songmin Liu, Binchang Zhou, Lizhong Sun
- Link: https://arxiv.org/abs/2608.05529v1
- Score: 24.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 近两周发布

**中文摘要：** 迄今为止，交变磁性的研究主要集中在磁性材料中的自旋极化体电子态。在这项工作中，我们通过引入表面交变磁体（SAM）的概念来推进该领域，其中交变磁体自旋极化出现在共线反铁磁体（AFM）或交变磁体（AM）的表面。为了为这种现象奠定理论基础，我们构建了一个彻底的基于对称的框架，该框架系统地将两种类型系统的体自旋群与表面自旋群连接起来。 通过对称性分析，我们确定了所有能够支持 SAM 的对称破缺表面，确定了 35 个 $PT$ 对称 AFM 和 61 个体 AM 的不同情况。此外，我们还表明，203 个共线自旋空间群（包括 100 个不使用 $[C_2 \Vert P]$ 操作的共线自旋空间群和 103 个使用 $[C_2 \Vert P]$ 操作）允许通过分数平移对称性的破缺在 $tT$ 对称 AFM 的表面上出现 SAM。 所提出的框架使用紧束缚模型和第一原理计算进行了验证，并在 NaMnP、LiMnAs 和 CrSb 等代表性化合物中展示了实际材料的实现。我们的研究结果将 SAM 确立为一种强大的、对称保护的磁态，将交变磁现象扩展到材料表面，并为下一代自旋电子技术中先进的无场自旋操纵铺平了道路。
**讨论重点：** 为了为这种现象奠定理论基础，我们构建了一个彻底的基于对称的框架，该框架系统地将两种类型系统的体自旋群与表面自旋群连接起来。在这项工作中，我们通过引入表面交变磁体（SAM）的概念来推进该领域，其中交变磁体自旋极化出现在共线反铁磁体（AFM）或交变磁体（AM）的表面。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Type-II Mirror Chern Insulator in Altermagnets

- Source: arXiv
- Date: 2026-08-07T16:16:42Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Amrita Mukherjee, Pritesh Srivastava, Rahul Verma, Bahadur Singh
- Link: https://arxiv.org/abs/2608.07374v1
- Score: 22.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 尽管净磁化强度为零，但具有动量相关自旋分裂的交变磁体可以在打破时间反转对称性的情况下支持独特的拓扑状态。我们预测二维交替磁体中具有动量分离边缘模式的镜像对称保护的拓扑晶体绝缘体。使用方八边形晶格模型，我们证明交变磁序生成对称相关的谷极化狄拉克节点，这些节点通过自旋轨道耦合产生间隙，产生$C_{\mathcal{M}}=2$的镜陈绝缘体。 传统的镜陈绝缘体中，两个镜面保护的边缘模式以相同的动量交叉形成狄拉克锥，与此相反，交变磁自旋分裂和谷选择性能带反转将这些边缘模式的动量分开。我们将此相称为 II 型镜陈绝缘体。我们进一步提出 PbSe/$\mathrm{V_2Se_2O}$ 异质双层作为通过交变邻近效应实现该相的候选材料。我们的结果确立了交变磁学是通向具有动量分离边缘模式的镜面保护拓扑相的途径。
**讨论重点：** 我们进一步提出 PbSe/$\mathrm{V_2Se_2O}$ 异质双层作为通过交变邻近效应实现该相的候选材料。使用方八边形晶格模型，我们证明交变磁序生成对称相关的谷极化狄拉克节点，这些节点通过自旋轨道耦合产生间隙，产生$C_{\mathcal{M}}=2$的镜陈绝缘体。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Topological surface altermagnets in SSH-stacked magnetic layers

- Source: arXiv
- Date: 2026-08-07T10:46:33Z
- Venue: cond-mat.mes-hall
- Authors: Rui Chen, Bin Zhou, Dong-Hui Xu
- Link: https://arxiv.org/abs/2608.07099v1
- Score: 22.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 表面交变磁性通过在传统反铁磁体的边界解锁交变磁性自旋分裂，绕过块体交变磁体的严格对称性要求，为自旋电子学开辟了新的途径。在这项工作中，我们建议通过以 Su-Schrieffer-Heeger 模式堆叠磁性层来创建拓扑表面交替磁体。 我们表明，虽然系统的大部分是标准反铁磁体，具有受 $PT$ 对称性保护的简并能带，但打破边界处的局部对称性会在拓扑间隙内产生拓扑保护的表面交变磁态。此外，我们建议可以通过施加垂直电场来通过实验检测到这种效应。此外，这种方法可以很容易地推广到不同类型的表面交变磁性。 我们的工作将拓扑边界建立为表面交变磁体的自然平台，为实现和操纵拓扑表面交变磁体提供了独特的途径。
**讨论重点：** 在这项工作中，我们建议通过以 Su-Schrieffer-Heeger 模式堆叠磁性层来创建拓扑表面交替磁体。此外，这种方法可以很容易地推广到不同类型的表面交变磁性。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Correlated topological-polarization surface states in the narrow-gap insulator FeSb2

- Source: arXiv
- Date: 2026-08-06T11:11:43Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Takahiro Iwagaki, Hideki Matsuoka, Ginta Hoshino, Kanata Watanabe, Shungo Aoyagi, Shunsuke Kitou
- Link: https://arxiv.org/abs/2608.05887v1
- Score: 14.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 强电子相关性和能带拓扑都产生丰富的量子相，但相互冲突的元素要求在很大程度上使它们分开。拓扑极化提供了一种将它们结合起来的途径，在没有自旋轨道耦合的情况下从键合电荷产生极性表面态，从而将能带拓扑扩展到相关的 3d 过渡金属化合物。在这里，我们证明了窄间隙绝缘体 FeSb2 的外延薄膜具有拓扑极化起源的金属极性表面态，受块体的强相关性控制。 非互易表面传输仅出现在相关驱动的大块 Fe 3d 轨道占据重建的起始温度以下，提供了相关拓扑系统中大块边缘对应的直接证据。此外，静电门控驱动该相关表面通过量子相变进入铁磁态或可能的交磁态。我们的结果将拓扑极化确立为各种材料中相关拓扑相的设计原则。
**讨论重点：** 我们的结果将拓扑极化确立为各种材料中相关拓扑相的设计原则。拓扑极化提供了一种将它们结合起来的途径，在没有自旋轨道耦合的情况下从键合电荷产生极性表面态，从而将能带拓扑扩展到相关的 3d 过渡金属化合物。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Superconducting and charge-ordered phases from Dirac quantum spin liquids on the triangular lattice

- Source: arXiv
- Date: 2026-08-05T18:00:01Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Andreas Feuerpfeil, Ronny Thomale, Subir Sachdev, Pietro M. Bonetti
- Link: https://arxiv.org/abs/2608.05277v1
- Score: 14.0
- Match: 标题匹配 quantum spin liquid; 近两周发布

**中文摘要：** 三角晶格量子自旋液体绝缘体被观察到在压力或掺杂下经历超导转变，并在中红外光驱动时表现出增强的太赫兹电导率。我们提出了一个通用理论框架，用于从具有费米子自旋子的 U(1) 狄拉克自旋液体及其带隙 $\mathbb{Z}_2$ 和手性后代中出现超导和电荷有序相。数值研究为这些自旋液体状态提供了实质性证据。 自旋液相具有与新兴规范场耦合的分段狄拉克自旋子，而超导相和电荷有序相是传统的，既没有分段激励，也没有新兴规范动力学。这些相之间的转变是由无自旋电荷 $e$ 玻色子（“双布朗”和“完整子”）的希格斯凝聚驱动的。我们证明，狄拉克自旋子的射影对称群唯一地决定了电荷的对称性和色散，使我们能够在电荷带极小值附近构建有效的低能理论。 chargon 希格斯场的规范不变复合提供了表征相的序参数。所得相图包含丰富多样的有序态，包括 $d+id$ 超导性、电荷密度波、键密度波和对密度波。
**讨论重点：** 我们提出了一个通用理论框架，用于从具有费米子自旋子的 U(1) 狄拉克自旋液体及其带隙 $\mathbb{Z}_2$ 和手性后代中出现超导和电荷有序相。数值研究为这些自旋液体状态提供了实质性证据。 结合关键词看，阅读时应重点关注量子自旋液体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 6. Lifting the degeneracy of quantum spin liquid phase by uniaxial pressure

- Source: arXiv
- Date: 2026-08-05T12:49:04Z
- Venue: cond-mat.str-el
- Authors: Shams Sohel Islam, Zurab Guguchia, Orion Gerguri, Petr Král, Maxime Lamotte, Toni Shiroka
- Link: https://arxiv.org/abs/2608.04782v1
- Score: 14.0
- Match: 标题匹配 quantum spin liquid; 近两周发布

**中文摘要：** 我们报告了候选三维（3D）量子自旋液体（QSL）PbCuTe$_2$O$_6$的μ子自旋弛豫/旋转（$μ$SR）测量，其承载$S=1/2$矩，在受控原位[110]单轴压缩下高达$σ_{[110]}=37.7$~MPa。小的方向晶格扰动会显着改变局部磁响应，而在 $σ_{\rm cr}\sim10.8$\,MPa 以上时，弛豫率会大大增强，内场分布也会显着拓宽。这些变化随着局部晶体对称性破缺而发生。 虽然没有观察到传统静态长程磁序的证据，但压缩驱动系统走向结构修改和强相关状态，其中增强的准静态相关性与持续的慢自旋动力学共存。这项工作展示了一种干净且对称选择性的路线，可以控制受挫的​​交换景观并访问 3D QSL 候选物中隐藏的磁不稳定性，从而为调整其他相关系统提供了可能性，其中磁自由度和晶格自由度之间的内在耦合是相关的。
**讨论重点：** 我们报告了候选三维（3D）量子自旋液体（QSL）PbCuTe$_2$O$_6$的μ子自旋弛豫/旋转（$μ$SR）测量，其承载$S=1/2$矩，在受控原位[110]单轴压缩下高达$σ_{[110]}=37.7$~MPa。小的方向晶格扰动会显着改变局部磁响应，而在 $σ_{\rm cr}\sim10.8$\,MPa 以上时，弛豫率会大大增强，内场分布也会显着拓宽。 结合关键词看，阅读时应重点关注量子自旋液体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Exploring the Relaxation Landscape of a 2D Quantum Magnet on a 256-Qubit Processor

- Source: arXiv
- Date: 2026-08-07T12:48:43Z
- Venue: quant-ph, cond-mat.mtrl-sci
- Authors: Tiago Mendes-Santos, Joseph Vovrosh, Sergi Julià-Farré, Dorian Claveau, Guillaume Villaret, Lucas Béguin
- Link: https://arxiv.org/abs/2608.07178v1
- Score: 12.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 量子物质如何远离平衡态松弛是多体物理学中的一个核心开放问题，对于这个问题，模拟量子模拟器能够很好地从证实理论转向发现新物理。在这里，我们使用 256 个量子位的二维里德堡原子阵列来绘制二维横向场伊辛模型在其相图上的弛豫图。除了预期的快速热化之外，我们还确定了另外两种状态。第一个是预热态，其动力学由有效的 XY 模型控制。 第二种，也是最出乎意料的，是一种交叉机制，其特征是松弛速度减慢。这种减速恰恰发生在最先进的经典张量网络方法在后期失去控制的情况下，而量子模拟在不同系统规模上保持一致。这些结果将里德伯原子阵列确立为非平衡量子多体动力学科学发现的平台。
**讨论重点：** 在这里，我们使用 256 个量子位的二维里德堡原子阵列来绘制二维横向场伊辛模型在其相图上的弛豫图。除了预期的快速热化之外，我们还确定了另外两种状态。 结合关键词看，阅读时应重点关注量子多体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 8. Many-Body Mobility Edge and Non-Hermitian Skin Effect in an Interacting Quasi-Periodic Spin Chain

- Source: arXiv
- Date: 2026-08-07T10:34:17Z
- Venue: cond-mat.dis-nn, cond-mat.str-el, quant-ph
- Authors: Lavoisier Wah, Ayan Banerjee, Flore K. Kunst
- Link: https://arxiv.org/abs/2608.07083v1
- Score: 12.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 非厄米多体物理学揭示了拓扑、局域化和边界效应之间丰富的相互作用，但它们在相互作用的无序系统中的集体行为在很大程度上仍未被探索。在这项工作中，我们研究了受准周期纵向场影响的相互作用的非厄米自旋链，提供了一个统一且受控的设置，其中非厄米动力学、相互作用和局部化机制交织在一起。 值得注意的是，我们发现了一个“D 形”多体移动边缘，它将扩展和局部本征态分开，同时描绘了多体局域化和多体趋肤效应（其中多体本征态在开放边界下向边界产生异常漂移）的区域，这些边界是由相互作用、非厄米性和驱动振幅的综合作用产生的。我们证明趋肤效应会在非厄米特本征态中引起多重分形缩放，从而提供多体趋肤效应的清晰特征。 采用分形维数、复特征值分数和多体逆参与比等诊断方法，我们绘制了一个统一的相图，其中所有测量一致地识别“D 形”移动边缘。最后，我们使用复杂的能级间距统计数据和动态可观测值（例如密度不平衡、纠缠增长和波包演化）来探讨这种相互作用，最终形成丰富的多体移动相图，捕获多体趋肤效应和局域化转变。 我们的研究结果确定了“D 形”多体移动性边缘的清晰定义特征，并强调了其在塑造开放量子多体系统物理过程中的关键作用。
**讨论重点：** 在这项工作中，我们研究了受准周期纵向场影响的相互作用的非厄米自旋链，提供了一个统一且受控的设置，其中非厄米动力学、相互作用和局部化机制交织在一起。 值得注意的是，我们发现了一个“D 形”多体移动边缘，它将扩展和局部本征态分开，同时描绘了多体局域化和多体趋肤效应（其中多体本征态在开放边界下向边界产生异常漂移）的区域，这些边界是由相互作用、非厄米性和驱动振幅的综合作用产生的。 结合关键词看，阅读时应重点关注量子多体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 9. Anderson Orthogonality as Measurement Backaction in Coupled Quantum Dots

- Source: arXiv
- Date: 2026-08-06T20:05:40Z
- Venue: cond-mat.mes-hall
- Authors: Will Grant, Sarath Sankar, Elena Cornick, Vahid Movahed, Johann Drayne, Silvia Lüscher
- Link: https://arxiv.org/abs/2608.06550v1
- Score: 11.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 测量通过将量子系统耦合到外部自由度来扰动量子系统，但探测器的反作用取决于测量本身的物理机制。在固态设备中，探测器远离平衡驱动以实现更快的测量，从而产生反作用，通常可以将其理解为经典噪声。然而，即使没有散粒噪声，强测量也会引起探测器中测量固有的量子多体相关性的反作用。 在这里，我们通过量子点电荷传感器对第二个量子点与其储存库之间的隧道效应来探测这种近平衡反作用。该测量实现了安德森正交灾难（AOC）：探测器引线中的电子响应局部散射势的突然变化而重新组织，抑制共振隧道效应，同时实现与探测器交换能量的非弹性过程。改变探测器能量水平可将隧道动力学中的 AOC 反作用从可忽略调整为占主导地位。 更广泛地说，这些结果将探测器引起的多体相关性确立为对量子动力学的可控影响。
**讨论重点：** 测量通过将量子系统耦合到外部自由度来扰动量子系统，但探测器的反作用取决于测量本身的物理机制。在固态设备中，探测器远离平衡驱动以实现更快的测量，从而产生反作用，通常可以将其理解为经典噪声。 结合关键词看，阅读时应重点关注量子多体相关的样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释。

### 10. Excitonic Magnetism in Ruthenium Pyrochlores

- Source: arXiv
- Date: 2026-08-06T18:43:12Z
- Venue: cond-mat.str-el
- Authors: Swetlana Swarup, Yang Yang, Natalia B. Perkins
- Link: https://arxiv.org/abs/2608.06504v1
- Score: 11.0
- Match: 摘要匹配 Hubbard model; 最近 3 天发布

**中文摘要：** $d^4$ 系统中的强自旋轨道耦合有望稳定非磁性 $J=0$ 单线态基态，但许多钌烧绿石表现出强大的长程磁序。受这一明显矛盾的启发，我们发展了烧绿石晶格上范弗莱克激子磁性的微观理论。从具有自旋轨道耦合的多轨道哈伯德模型出发，我们推导了 Ru$^{4+}$ 离子的低能单重态-三重态流形内的有效超交换相互作用。 我们使用三重子激发光谱和凝聚相的变分处理来分析所得的激子哈密顿量。我们确定了非磁性单线态对三重态凝聚的不稳定性，并确定了所得的磁性相图作为微观跳跃参数的函数。该相图再现了从传统烧绿石模型中已知的磁序，同时还预测了单线态-三线态描述所特有的附加磁相。 最后，我们将该理论应用于烧绿石钌酸盐，特别是 Nd$_2$Ru$_2$O$_7$，并表明它非常接近激子量子临界点。我们的研究结果建立了一个微观框架，用于理解烧绿石钌酸盐中的激子磁性及其磁激发光谱，提供与光谱探针（包括拉曼散射）的直接连接。
**讨论重点：** 受这一明显矛盾的启发，我们发展了烧绿石晶格上范弗莱克激子磁性的微观理论。我们使用三重子激发光谱和凝聚相的变分处理来分析所得的激子哈密顿量。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。
