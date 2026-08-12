# Latest papers for 程旭丽

Updated: 2026-08-12T05:48:17.939780+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 13.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries

- Source: arXiv
- Date: 2026-08-07T07:36:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Timothée Jamin, Zhencai Li, Kasper Tolborg, Yuanzheng Yue
- Link: https://arxiv.org/abs/2608.06902v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 全固态锂电池需要将快速室温离子传输与机械鲁棒性和界面兼容性相结合的固体电解质。沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 这是通过使用机器学习原子间势来模拟晶体和玻璃态 ZIF-4 和 ZIF-62 中的 Li+ 传输来实现的。结构紊乱将 Li+ 迁移的活化能从约 0.35 eV 降低至 0.16 eV，并将 ZIF-4 的外推室温扩散系数增加了一个数量级以上，而 ZIF-62 则增加了近七倍。 非高斯动力学和范霍夫相关函数的分析表明，Li+在晶体ZIF中的扩散是通过明确的笼子之间罕见的、动态异质的跳跃事件发生的，而玻璃态ZIF中的Li+扩散更加均匀、连续和类似Fickian，受益于广泛分布的配位几何形状和迁移势垒。晶体 ZIF 中的 Li+ 扩散具有强烈的各向异性，这反映出咪唑盐和苯并咪唑盐环的有序取向沿不同的晶体方向施加了不同的能垒。 玻璃化后，这些环的方向变得随机，因此，Li + 的扩散变得各向同性或近各向同性。这些发现表明，精心设计的金属有机框架玻璃是高性能固态电解质的有希望的候选者。
**讨论重点：** 沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Local Structure Dictates Ionic Transport and Mechanical Properties in Glassy Solid Electrolytes for Lithium Batteries

- Source: arXiv
- Date: 2026-08-07T07:29:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Rasmus Christensen, Timothée Jamin, Zhencai Li, Qi Zhang
- Link: https://arxiv.org/abs/2608.06895v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 由硫化物和卤化物玻璃组成的电解质由于其可加工性、缺乏晶界和相对较高的离子电导率而成为全固态锂电池的有希望的候选者。然而，它们的离子电导率和机械性能仍然不能满足实际应用。固体电解质的重大进步需要对其微观结构的透彻了解。 在这里，我们通过采用基于机器学习原子间势的分子动力学模拟，揭示了一系列玻璃态固体电解质的结构、离子传输特性和机械稳定性之间的联系。具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。将 P2S5 引入 B2S3 基玻璃中会引发关键的结构转变，从而增强离子电导率和机械纳米延展性。 对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。同时，灵活的 P-S-P 配置可以通过键弯曲实现能量耗散，从而实现脆性到延性的转变。然而，过量的 P2S5 会增加多磷酸盐（例如 P2S6 和 P2S7）的比例，从而聚合结构网络并最终阻碍 Li+ 的迁移率。 因此，我们的工作为工程玻璃电解质提供了原子原理，具有平衡的离子电导率和机械鲁棒性。
**讨论重点：** 具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. An Exchange-Correlation Functional for Fast and Accurate Modeling of Ferroelectric Perovskites

- Source: arXiv
- Date: 2026-08-05T13:12:10Z
- Venue: cond-mat.mtrl-sci
- Authors: Owain T. Beynon, Chiara Gattinoni
- Link: https://arxiv.org/abs/2608.04806v1
- Score: 8.0
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
- Score: 29.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials

**中文摘要：** 由于其依赖于动量的自旋分裂，交变磁体最近成为自旋电子应用中有前途的材料。其中，金属CrSb因其巨大的自旋分裂和高尼尔温度而特别引人注目。然而，块状和薄膜 CrSb 中独特的自旋分裂行为的微观起源仍未解决。在这里，我们使用第一性原理计算系统地研究了具有不同表面取向的 CrSb 板的电子结构。 尽管所有考虑的板片都保留了与交变磁性兼容的自旋群对称性，但它们表现出明显不同的电子结构：(2$\bar{1}\bar{1}$0) 板片保留了明显的交变磁自旋分裂，而 (0001) 和 (10$\bar{1}$0) 板片显示出近自旋简并的能带。我们证明，降维从根本上改变了交变磁自旋分裂的微观起源。 与块状 CrSb 不同，薄膜中的交变磁自旋分裂需要长程晶胞间共面 Cr-Sb 跳跃，而 Sb-Sb 跳跃提供额外的贡献。这些跳跃路径的保留或抑制解释了自旋分裂的强烈表面依赖性。我们的研究结果建立了一种理解降维交变磁性的微观机制，并为低维交变磁性材料中的工程自旋分裂提供了一般原理。
**讨论重点：** 在这里，我们使用第一性原理计算系统地研究了具有不同表面取向的 CrSb 板的电子结构。其中，金属CrSb因其巨大的自旋分裂和高尼尔温度而特别引人注目。 结合关键词看，阅读时应重点关注交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Competition between local magnetic disorder and altermagnetism in doped FeSb$_2$

- Source: arXiv
- Date: 2026-08-11T15:57:19Z
- Venue: cond-mat.mtrl-sci
- Authors: Enrico Di Lucente, Michele Simoncelli
- Link: https://arxiv.org/abs/2608.11089v1
- Score: 28.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 最近的实验报告表明，窄带隙非磁性半导体FeSb$_2$可以通过Co掺杂（Co$_{0.15}$Fe$_{0.85}$Sb$_2$）转变为交磁金属，或者通过Cr掺杂转变为磁无序或短程有序状态（Cr$_{0.15}$Fe$_{0.85}$Sb$_2$）。在这里，我们依靠哈伯德增强密度泛函理论（DFT+U）结合罗密欧基态搜索算法，从第一原理探索这些掺杂系统的能量景观和磁态。 在已建立的虚拟晶体近似（VCA）中，我们表明 \texttt{Romeo} 发现了几个不平凡的磁态，这些磁态为超级晶胞中掺杂的有针对性的显式模拟提供了信息。我们依靠这些发现来讨论 VCA-Romeo 方法与显式掺杂超级细胞方法的优点和局限性，以及如何协同使用它们。 总体而言，我们的模拟表明，Cr 掺杂系统的基态是局域无序自旋补偿 (LDSC) 配置，形式上与 Néel 的 L 型完全补偿亚铁磁性兼容，而 Co 掺杂系统的基态被发现是交变磁性 (AFMo)。这项工作展示了磁性合金的近似和显式模拟如何能够相互提供信息，并建立了研究候选金属交替磁体的协议。
**讨论重点：** 在这里，我们依靠哈伯德增强密度泛函理论（DFT+U）结合罗密欧基态搜索算法，从第一原理探索这些掺杂系统的能量景观和磁态。我们依靠这些发现来讨论 VCA-Romeo 方法与显式掺杂超级细胞方法的优点和局限性，以及如何协同使用它们。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Time-Reversal-Invariant Altermagnetic Acoustic Crystals

- Source: arXiv
- Date: 2026-08-09T17:20:24Z
- Venue: cond-mat.mes-hall
- Authors: Tianzhi Xia, Han-Rong Xia, Jinglin Liu, Xiying Fan, Zebin Zhu, Zhen Gao
- Link: https://arxiv.org/abs/2608.08827v1
- Score: 26.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交替磁体已成为一类新型磁性材料，它将自旋分裂电子​​带与零净磁化强度结合在一起。然而，将这种范式扩展到经典波系统从根本上来说是具有挑战性的，因为传统的实现需要打破时间反转对称性（TRS）。在这里，我们通过引入两个赝自旋自由度并构建一个赝时间反转算子来克服这一限制，该算子忠实地再现其物理对应物的动作，同时保留实际的 TRS。 在此框架的基础上，我们从理论上提出并通过实验实现了第一个时间反转不变的交变磁声晶体。声学测量直接揭示了在严格保留 TRS 的条件下赝自旋相关的能带分裂——交变磁力的一个定义标志。此外，交变磁声晶体表现出亚晶格赝自旋锁定，能够灵活控制声学赝自旋分裂和滤波。 我们的工作将声学晶体建立为探索交磁物理的多功能平台，并为非磁性设备中自旋激发的波操纵开辟了新途径。
**讨论重点：** 在此框架的基础上，我们从理论上提出并通过实验实现了第一个时间反转不变的交变磁声晶体。然而，将这种范式扩展到经典波系统从根本上来说是具有挑战性的，因为传统的实现需要打破时间反转对称性（TRS）。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Spin Splitter without Spin-Split Bands: A Reconfigurable Altermagnetic Texture

- Source: arXiv
- Date: 2026-08-11T14:25:24Z
- Venue: cond-mat.str-el
- Authors: Bin Xi, Jie Lu, Qiang Luo, Ken Chen, Jia-Wei Mei, Hong-Gang Luo
- Link: https://arxiv.org/abs/2608.10958v1
- Score: 25.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁自旋分离器效应将电场转换为横向纯自旋电流，没有净磁化，也没有电荷霍尔对应物。在已建立的材料中，该功能与晶体固定的自旋分裂带有关，该带将偏振轴锁定在晶格上。我们证明了受抑蜂窝磁体的非共面反螺旋基态通过 $\mathbf Q$ 锁定的螺旋镜 $g$ 进行交变磁操作。 镜子选择自旋流偏振并禁止垂直偏振，而反平移$θ$则禁止偶宇称自旋分裂。因此，能带分裂和自旋分裂响应依赖于不同的对称元素。任一元件单独强制电荷霍尔为零——其他自旋轨道非共线路线中不存在的冗余——并且仅当两个元件都被移除时电荷霍尔才会出现。 然后，空穴掺杂实现了一个\emph{没有自旋分裂能带的自旋分裂器}——在费米能级处跳跃$t$的对称性允许的奇宇称残差低于$2\times10^{-7}$——其中$σ_H^{(s_y)}=0.082\,e^2/h$没有自旋轨道耦合和零电荷霍尔响应。在三个简并 $\mathbf{Q}$ 方向中进行选择，以固定幅度和电荷霍尔为零的精确 $120^\circ$ 步长旋转偏振轴；选择规则保留在可访问可编程光子和电路晶格的 32 美元站点单元中。
**讨论重点：** 交变磁自旋分离器效应将电场转换为横向纯自旋电流，没有净磁化，也没有电荷霍尔对应物。在已建立的材料中，该功能与晶体固定的自旋分裂带有关，该带将偏振轴锁定在晶格上。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 5. Magnetotransport evolution and nonlinear Hall effect in altermagnetic MnTe

- Source: arXiv
- Date: 2026-08-10T09:49:13Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn, cond-mat.str-el
- Authors: Wei Zhou, Zhifeng Xue, Yunxing Li, Nannan Tang, Ye Tao, Dingyong Zhong
- Link: https://arxiv.org/abs/2608.09371v1
- Score: 24.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 六方锰碲是一种典型的半导体交变磁体，其特性受到内在无序的严重影响，但由此产生的不同输运机制如何塑造其磁输运行为以及相对论自旋轨道耦合（SOC）的作用仍有待澄清。在这里，我们对 MnTe 块状单晶中的各向异性磁阻 (AMR)、平面霍尔效应 (PHE) 和非线性输运进行了系统研究。 在尼尔温度 (TN ~ 304 K) 以下，高温金属状态下 AMR 和 PHE 中高阶谐波的出现揭示了磁序、晶体对称性和 SOC 的相互作用。在相对较低的温度下，高阶对称性的消失与传输交叉进入跳跃传导状态同时发生，这表明载流子局域化降低了对费米表面拓扑的传输敏感性。 此外，我们还检测到了独特的二阶非线性霍尔信号，为互磁 MnTe 中的宏观反演不对称响应提供了证据。将研究扩展到局部区域，为了解无序和 SOC 在宏观电荷传输中的微妙作用提供了重要见解。因此，我们的工作强调了探索跨不同传导机制的磁输运以全面了解交磁特性的必要性。
**讨论重点：** 在这里，我们对 MnTe 块状单晶中的各向异性磁阻 (AMR)、平面霍尔效应 (PHE) 和非线性输运进行了系统研究。在尼尔温度 (TN ~ 304 K) 以下，高温金属状态下 AMR 和 PHE 中高阶谐波的出现揭示了磁序、晶体对称性和 SOC 的相互作用。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Altermagnetism-Induced Spin-resolved electronic structure in Janus FeX0.5Y0.5 Monolayers (X, Y = S, Se, Te)

- Source: arXiv
- Date: 2026-08-10T03:00:42Z
- Venue: cond-mat.mtrl-sci
- Authors: Mengyang Zhang, Jie Li, Yifei Chen, Shifang Li, Zhentao Fu, Jianxin Zhong
- Link: https://arxiv.org/abs/2608.09054v1
- Score: 23.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 实现超导材料中的自旋分辨电子特性是一个关键前沿，它为无耗散自旋器件提供了新颖的基础物理和潜力。在这里，我们通过使用近藤型模型和第一性原理计算预测了一系列源自铁基超导体（例如 FeSe、FeTe 和 FeS）的 Janus FeX0.5Y0.5 单层。这些 Janus 结构表现出显着的自旋分裂电子​​态、大的拓扑带隙 (51.4 meV) 和高尼尔温度 (415 K)。 我们进一步揭示，可以通过施加面内应变来有效地调节谷极化，并且可以通过改变费米能级来操纵由此产生的谷极化反常霍尔电导率。我们的工作提出了一种基于交变磁性的新策略，用于在超导系统中设计自旋分裂态，并激发了对超导自旋电子学的进一步探索。
**讨论重点：** 在这里，我们通过使用近藤型模型和第一性原理计算预测了一系列源自铁基超导体（例如 FeSe、FeTe 和 FeS）的 Janus FeX0.5Y0.5 单层。这些 Janus 结构表现出显着的自旋分裂电子​​态、大的拓扑带隙 (51.4 meV) 和高尼尔温度 (415 K)。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Floquet Engineering of Topological Phases and Magneto-Optical Response in a Driven $d$-wave Altermagnet

- Source: arXiv
- Date: 2026-08-11T17:51:05Z
- Venue: cond-mat.mes-hall
- Authors: Muzamil Shah
- Link: https://arxiv.org/abs/2608.11192v1
- Score: 18.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究了 Floquet 线性偏振光驱动如何控制二维 (2D) $d$ 波交变磁体的拓扑和磁光响应。在没有线性偏振光场和自旋守恒的情况下，我们发现该系统具有自旋陈（量子自旋霍尔模拟）相，两个自旋扇区中的陈数具有相反的符号。照射光场打破了自旋扇区之间的 $C_{4z}\mathcal{T}$ 晶体反统一对称性。 对称性破缺源自偏振相关的 Peierls 相，它沿两个轴各向异性地重新规范化跳跃。由此产生的自旋选择性间隙闭合产生中间陈绝缘相 $C=\pm1$。驱动幅度 $A_0$ 决定反转阈值，而将偏振旋转 $π/2$ 会交换自旋扇区并反转陈数。使用久保形式主义，我们计算了频率相关的纵向电导率和霍尔电导率，并导出了独立式导电片的相应法拉第和克尔旋转。 纵向响应跟踪 Floquet 重整化带间阈值，而光学霍尔响应与磁光旋转的符号一起区分两个相反的贝里曲率手性。相当大的克尔角仅出现在狭窄的共振窗口内，并且应与反射强度和克尔椭圆率一起解释。这些结果表明，线偏振光可作为 d$ 波交替磁体中自旋分辨能带反转、陈数转换和非接触式光学检测的对称选择手柄。
**讨论重点：** 我们研究了 Floquet 线性偏振光驱动如何控制二维 (2D) $d$ 波交变磁体的拓扑和磁光响应。在没有线性偏振光场和自旋守恒的情况下，我们发现该系统具有自旋陈（量子自旋霍尔模拟）相，两个自旋扇区中的陈数具有相反的符号。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 8. Quantum Mechanism of Piezomagnetism in Higher-Spin Altermagnets

- Source: arXiv
- Date: 2026-08-11T09:54:41Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Daisuke Yamamoto, Makoto Naka
- Link: https://arxiv.org/abs/2608.10735v1
- Score: 18.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们使用味道波方法研究具有易平面单离子各向异性的高自旋交变磁体中的压磁性。我们表明，高自旋集体模式的量子涨落提供了压磁响应的微观起源。对于整数自旋，相关分支在接近大$D$转变时软化并演变成类希格斯振幅模式，赋予激发相当大的偶极分量并产生压磁性的显着增强。 相比之下，在半整数系统中，随着各向异性的增加，高自旋分支逐渐与低能偶极扇区分离，这抑制了它们对响应的贡献。这种整数-半整数对比将宏观压磁性与多极激发的低能命运直接联系起来。我们的结果将压磁学确立为高自旋量子动力学的探针，并将高自旋交变磁体确定为量子磁弹性响应的有希望的设置。
**讨论重点：** 我们使用味道波方法研究具有易平面单离子各向异性的高自旋交变磁体中的压磁性。我们表明，高自旋集体模式的量子涨落提供了压磁响应的微观起源。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Some features of high-temperature superconductivity on flat bands

- Source: arXiv
- Date: 2026-08-10T21:08:33Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: V. R. Shaginyan, A. Z. Msezane, S. A. Artamonov
- Link: https://arxiv.org/abs/2608.10231v1
- Score: 17.0
- Match: 标题匹配 high-temperature superconductivity; 最近 3 天发布

**中文摘要：** 在这封信中，我们研究了即使在排斥配对相互作用的情况下，平带的存在如何导致高温超导体的形成。我们还表明，在平带的情况下，高温超导状态使平带变形，使其倾斜并使有效质量有限。结果，超流体重量和超电流都没有消失。我们的结果与实验数据非常吻合。
**讨论重点：** 在这封信中，我们研究了即使在排斥配对相互作用的情况下，平带的存在如何导致高温超导体的形成。我们还表明，在平带的情况下，高温超导状态使平带变形，使其倾斜并使有效质量有限。 结合关键词看，阅读时应重点关注高温超导相关的样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释。

### 10. A spin-bond theory unifying non-relativistic spin splitting and emergent spin-orbit textures

- Source: arXiv
- Date: 2026-08-10T14:22:59Z
- Venue: cond-mat.mtrl-sci
- Authors: S. Allende, R. M. Otxoa
- Link: https://arxiv.org/abs/2608.09644v1
- Score: 16.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 净磁化强度消失的磁序可以产生非相对论性自旋分裂带，大致分为偶宇称交替磁体和奇宇称\(p\)波磁体。在这里，我们引入了一种自旋键理论，它将这些看似不同的现象统一到一个代数框架中。我们证明非相对论性自旋纹理从根本上由电子键的两个组成部分控制：酉自旋相位和厄米自旋振幅。 酉扇区产生奇宇称 p 波和涌现的自旋轨道状纹理，而厄米扇区产生偶宇称自旋场，包括均匀的\(\)分裂和键结构的交磁极限。除了统一已知相之外，我们的理论还揭示了当酉扇区和厄米扇区无法交换时出现的混合非交换状态，揭示了潜在的非交换自旋键结构。 这种状态产生了一种非共面的自旋纹理，其特征是动量均匀的横向自旋极化，为自旋和角度分辨的光电子能谱提供了直接的光谱指纹。此外，我们确定这种合成自旋轨道耦合可以通过几何控制键合扇区的非交换来动态调整。通过为这种调谐提供微观基础，我们的理论为包括无场自旋量子位在内的高级应用铺平了道路。
**讨论重点：** 在这里，我们引入了一种自旋键理论，它将这些看似不同的现象统一到一个代数框架中。我们证明非相对论性自旋纹理从根本上由电子键的两个组成部分控制：酉自旋相位和厄米自旋振幅。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
