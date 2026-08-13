# Latest papers for 程旭丽

Updated: 2026-08-13T05:52:58.282142+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 12.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 2. Fast Isotropic Li-Ion Diffusion in Zeolitic Imidazolate Framework Glass Electrolytes for Batteries

- Source: arXiv
- Date: 2026-08-07T07:36:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Timothée Jamin, Zhencai Li, Kasper Tolborg, Yuanzheng Yue
- Link: https://arxiv.org/abs/2608.06902v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 全固态锂电池需要将快速室温离子传输与机械鲁棒性和界面兼容性相结合的固体电解质。沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 这是通过使用机器学习原子间势来模拟晶体和玻璃态 ZIF-4 和 ZIF-62 中的 Li+ 传输来实现的。结构紊乱将 Li+ 迁移的活化能从约 0.35 eV 降低至 0.16 eV，并将 ZIF-4 的外推室温扩散系数增加了一个数量级以上，而 ZIF-62 则增加了近七倍。 非高斯动力学和范霍夫相关函数的分析表明，Li+在晶体ZIF中的扩散是通过明确的笼子之间罕见的、动态异质的跳跃事件发生的，而玻璃态ZIF中的Li+扩散更加均匀、连续和类似Fickian，受益于广泛分布的配位几何形状和迁移势垒。晶体 ZIF 中的 Li+ 扩散具有强烈的各向异性，这反映出咪唑盐和苯并咪唑盐环的有序取向沿不同的晶体方向施加了不同的能垒。 玻璃化后，这些环的方向变得随机，因此，Li + 的扩散变得各向同性或近各向同性。这些发现表明，精心设计的金属有机框架玻璃是高性能固态电解质的有希望的候选者。
**讨论重点：** 沸石咪唑酯骨架 (ZIF) 玻璃（ZIF 是金属有机骨架的子集）提供了一个有吸引力但相对尚未开发的平台，因为它们将无晶界和无定形拓扑与化学可调骨架结合在一起。在这里，我们揭示了结构无序可以在 ZIF 玻璃中实现快速且各向同性的锂扩散。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Local Structure Dictates Ionic Transport and Mechanical Properties in Glassy Solid Electrolytes for Lithium Batteries

- Source: arXiv
- Date: 2026-08-07T07:29:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Yong Li, Tao Du, Rasmus Christensen, Timothée Jamin, Zhencai Li, Qi Zhang
- Link: https://arxiv.org/abs/2608.06895v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 由硫化物和卤化物玻璃组成的电解质由于其可加工性、缺乏晶界和相对较高的离子电导率而成为全固态锂电池的有希望的候选者。然而，它们的离子电导率和机械性能仍然不能满足实际应用。固体电解质的重大进步需要对其微观结构的透彻了解。 在这里，我们通过采用基于机器学习原子间势的分子动力学模拟，揭示了一系列玻璃态固体电解质的结构、离子传输特性和机械稳定性之间的联系。具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。将 P2S5 引入 B2S3 基玻璃中会引发关键的结构转变，从而增强离子电导率和机械纳米延展性。 对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。同时，灵活的 P-S-P 配置可以通过键弯曲实现能量耗散，从而实现脆性到延性的转变。然而，过量的 P2S5 会增加多磷酸盐（例如 P2S6 和 P2S7）的比例，从而聚合结构网络并最终阻碍 Li+ 的迁移率。 因此，我们的工作为工程玻璃电解质提供了原子原理，具有平衡的离子电导率和机械鲁棒性。
**讨论重点：** 具体来说，我们探索了玻璃态 Li-S-P-B-I (LSPBI) 中 B-S 和 P-S 网络之间的相互作用如何控制离子电导率和变形行为。对于中等 P2S5 含量，掺入的 PS4 单元可解聚刚性硼骨架，为快速离子传输创造渗透扩散路径。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 5. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 6. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 9. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 耐火高熵合金由于其优异的机械性能而成为高温应用的有希望的候选者。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。在这项工作中，通过利用通用机器学习原子间势与混合蒙特卡罗和分子动力学模拟，研究了(MoCrTi)(100-x)Alx系统的温度依赖性热力学和机械性能。 热容和短程有序参数揭示了不同的有序-无序转变行为。虽然 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出由 B2 型原子对的协同排序主导的单一转变，但 Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 合金表现出两个单独的转变：由特定对驱动的低温阶段（Mo28Cr28Ti28Al16 中的 Mo-Al；Mo28Cr28Ti28Al16 中的 Al-Al） Mo30Cr30Ti30Al10) 和由其余对控制的高温阶段。 结构分析表明，在低温有序B2相中，Mo和Al共享一个亚晶格，而Cr和Ti共享另一个亚晶格。此外，还确定了排序和机械刚度之间的关系。有序显着增强了弹性常数和模量，并产生非单调的成分依赖性。与随机固溶体不同的是，随机固溶体的刚度随着 Al 含量的降低而单调增加，有序构型表现出非单调趋势，在 Mo30Cr30Ti30Al10 合金中达到峰值。 这种增强归因于强短程有序引起的刚性原子对的优化群体。这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。
**讨论重点：** 这些发现为成分、化学排序和机械性能之间的相互作用提供了基本见解，为难熔高熵合金的设计提供了指导。了解这些复杂系统中化学排序背后的热力学机制对于优化其性能至关重要。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 10. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。优化的内存管理策略消除了传统上与远程交互相关的训练开销，从而使 4G-HDNNP 能够以与本地对应物相同的效率进行训练。 RuNNer 2.0 采用现代 Fortran（2003/2008 标准）开发，结合​​混合 MPI/OpenMP 并行化方案，旨在在任何 CPU 环境（从经济高效的本地工作站到大规模 HPC 集群）中高效运行。其模块化库架构有助于直接绑定到外部模拟软件； LAMMPS 和原子仿真环境 (ASE) 的本机接口提供对其所有功能的完全访问，包括内置的基于委员会的不确定性量化。 RuNNer 2.0生态系统的高效率和可扩展性通过详细的基准测试得到证明。
**讨论重点：** 我们推出了 RuNNer 2.0，即“鲁尔大学神经网络能量表示”，这是一款高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络电位 (HDNNP)。 用于描述第四代 (4G) HDNNP 中非局域电荷转移的远程静电和电荷平衡 (QEq) 通过准线性缩放平面波方法加速，将 QEq 计算复杂性从 $\mathcal{O}(N^3)$ 降低到 $\mathcal{O}(N\log^2 N)$，从而在所有 HDNNP 代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Two routes to quantum anomalous Hall states in altermagnets

- Source: arXiv
- Date: 2026-08-12T14:42:18Z
- Venue: cond-mat.str-el, cond-mat.mes-hall
- Authors: Makoto Naka, Shuntaro Sumita, Yukitoshi Motome, Hitoshi Seo
- Link: https://arxiv.org/abs/2608.12124v1
- Score: 27.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials

**中文摘要：** 我们从理论上提出了在交变磁材料中实现量子反常霍尔态的两种可能途径。我们考虑具有与斜方晶体结构相关的反对称自旋轨道耦合的最小方格哈伯德模型，该模型支持拓扑平凡的交变磁态。通过结合 Rashba 型自旋轨道耦合和外部扰动，我们证明了这种平凡的状态可以通过两种不同的方式转变为拓扑交磁相。 第一条路线由交错电势驱动，该电势打破了连接晶体等效子晶格的对称性，从而产生以量子化霍尔电导率 $\left| 为特征的拓扑交变磁基态。 σ_{xy} \right|=e^2/h$ 和陈数 $C=1$。第二条路线是通过施加垂直于二维平面的磁场来实现的。由此产生的拓扑状态在磁滞回线中显示为亚稳态，表现出量子化霍尔电导率 $\left| σ_{xy} \right|=2e^2/h$ 与陈数 $C=2$ 相关。 我们表明，这些拓扑转变伴随着布里渊区边界处的特征间隙闭合，间隙闭合点的数量决定了陈数。带状几何计算揭示了与体拓扑不变量一致的手性边缘态，并证明了 $C=1$ 和 $C=2$ 态之间不同的自旋极化。我们的结果建立了实验上可行的途径来实现交流磁体中的量化异常霍尔响应。
**讨论重点：** 我们从理论上提出了在交变磁材料中实现量子反常霍尔态的两种可能途径。我们考虑具有与斜方晶体结构相关的反对称自旋轨道耦合的最小方格哈伯德模型，该模型支持拓扑平凡的交变磁态。 结合关键词看，阅读时应重点关注Hubbard 模型、交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Competition between local magnetic disorder and altermagnetism in doped FeSb$_2$

- Source: arXiv
- Date: 2026-08-11T15:57:19Z
- Venue: cond-mat.mtrl-sci
- Authors: Enrico Di Lucente, Michele Simoncelli
- Link: https://arxiv.org/abs/2608.11089v1
- Score: 27.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 最近的实验报告表明，窄带隙非磁性半导体FeSb$_2$可以通过Co掺杂（Co$_{0.15}$Fe$_{0.85}$Sb$_2$）转变为交磁金属，或者通过Cr掺杂转变为磁无序或短程有序状态（Cr$_{0.15}$Fe$_{0.85}$Sb$_2$）。在这里，我们依靠哈伯德增强密度泛函理论（DFT+U）结合罗密欧基态搜索算法，从第一原理探索这些掺杂系统的能量景观和磁态。 在已建立的虚拟晶体近似（VCA）中，我们表明 \texttt{Romeo} 发现了几个不平凡的磁态，这些磁态为超级晶胞中掺杂的有针对性的显式模拟提供了信息。我们依靠这些发现来讨论 VCA-Romeo 方法与显式掺杂超级细胞方法的优点和局限性，以及如何协同使用它们。 总体而言，我们的模拟表明，Cr 掺杂系统的基态是局域无序自旋补偿 (LDSC) 配置，形式上与 Néel 的 L 型完全补偿亚铁磁性兼容，而 Co 掺杂系统的基态被发现是交变磁性 (AFMo)。这项工作展示了磁性合金的近似和显式模拟如何能够相互提供信息，并建立了研究候选金属交替磁体的协议。
**讨论重点：** 在这里，我们依靠哈伯德增强密度泛函理论（DFT+U）结合罗密欧基态搜索算法，从第一原理探索这些掺杂系统的能量景观和磁态。我们依靠这些发现来讨论 VCA-Romeo 方法与显式掺杂超级细胞方法的优点和局限性，以及如何协同使用它们。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Spin Splitter without Spin-Split Bands: A Reconfigurable Altermagnetic Texture

- Source: arXiv
- Date: 2026-08-11T14:25:24Z
- Venue: cond-mat.str-el
- Authors: Bin Xi, Jie Lu, Qiang Luo, Ken Chen, Jia-Wei Mei, Hong-Gang Luo
- Link: https://arxiv.org/abs/2608.10958v1
- Score: 24.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁自旋分离器效应将电场转换为横向纯自旋电流，没有净磁化，也没有电荷霍尔对应物。在已建立的材料中，该功能与晶体固定的自旋分裂带有关，该带将偏振轴锁定在晶格上。我们证明了受抑蜂窝磁体的非共面反螺旋基态通过 $\mathbf Q$ 锁定的螺旋镜 $g$ 进行交变磁操作。 镜子选择自旋流偏振并禁止垂直偏振，而反平移$θ$则禁止偶宇称自旋分裂。因此，能带分裂和自旋分裂响应依赖于不同的对称元素。任一元件单独强制电荷霍尔为零——其他自旋轨道非共线路线中不存在的冗余——并且仅当两个元件都被移除时电荷霍尔才会出现。 然后，空穴掺杂实现了一个\emph{没有自旋分裂能带的自旋分裂器}——在费米能级处跳跃$t$的对称性允许的奇宇称残差低于$2\times10^{-7}$——其中$σ_H^{(s_y)}=0.082\,e^2/h$没有自旋轨道耦合和零电荷霍尔响应。在三个简并 $\mathbf{Q}$ 方向中进行选择，以固定幅度和电荷霍尔为零的精确 $120^\circ$ 步长旋转偏振轴；选择规则保留在可访问可编程光子和电路晶格的 32 美元站点单元中。
**讨论重点：** 交变磁自旋分离器效应将电场转换为横向纯自旋电流，没有净磁化，也没有电荷霍尔对应物。在已建立的材料中，该功能与晶体固定的自旋分裂带有关，该带将偏振轴锁定在晶格上。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Dimensional crossover and local strain induced deflection of the spin spiral state in multiferroic NiI2

- Source: arXiv
- Date: 2026-08-12T11:32:08Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Tianxing Jiang, Lianchuang Li, Haiyan Zhu, Hongyu Wang, Junchao Tian, Wenzhao Wang
- Link: https://arxiv.org/abs/2608.11944v1
- Score: 21.0
- Match: 标题匹配 multiferroic; 摘要匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 低维多铁性材料对于集成磁电器件具有广阔的前景。最近，自旋螺旋态已被证明可以在单层范德华 (vdW) 材料 NiI2 中诱导铁电性。然而，这种状态如何演化以及如何调整至二维极限仍不清楚。在这里，我们结合自旋偏振扫描隧道显微镜、逐层薄膜生长和多尺度理论模型来研究 NiI2 薄膜中的自旋螺旋。 随着薄膜厚度从 1 单层增加到 7 个单层，我们观察到自旋螺旋波长不断增加，波矢量从近 [110] 方向旋转到 [1-10] 方向，这证明了主要由增强的层间交换能驱动的维度交叉。此外，我们发现薄膜皱纹会引起自旋螺旋波矢的偏转，这是由交换相互作用的局部曲率引起的修改引起的。 我们的研究结果将厚度和局部应变确定为工程非共线螺旋磁性和 vdW 多铁性材料中伴随电极化的两种调谐方法。
**讨论重点：** 在这里，我们结合自旋偏振扫描隧道显微镜、逐层薄膜生长和多尺度理论模型来研究 NiI2 薄膜中的自旋螺旋。最近，自旋螺旋态已被证明可以在单层范德华 (vdW) 材料 NiI2 中诱导铁电性。 结合关键词看，阅读时应重点关注多铁性、铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 5. Emergent heavy fermion and superconductivity near Mott transition in twisted bilayer graphene

- Source: arXiv
- Date: 2026-08-12T17:59:59Z
- Venue: cond-mat.str-el
- Authors: Ya-Hui Zhang
- Link: https://arxiv.org/abs/2608.12319v1
- Score: 18.0
- Match: 标题匹配 heavy fermion; 最近 3 天发布

**中文摘要：** 在带宽调谐莫特跃迁附近，金属的费米速度 $v_F$ 和准粒子残留 $Z$ 通常消失。在这里，我们展示了在整数填充时扭曲双层石墨烯（TBG）中出现的类似现象，并且可以通过投影有源带限制内的新兴重费米子框架捕获。与包含远程带的模型不同，我们有效的重费米子描述来自于 \textit{混合价莫特} 物理通过解耦电荷和局部矩扇区。 在电荷区域，活跃能带 $c(\mathbf{k})$ 与新兴的 \emph{正交费米子} $ψ(\mathbf{k})$ 杂交，在 $|\mathbf{k}| 处打开一个大的莫特能隙。 > k_*$ （$k_*$ 设置动量补丁大小）和中性点 ($ν=0$) 附近 $\mathbf{k}=0$ 附近的二次能带接触半金属。正交费米子是双克隆和完整子激励的线性组合，可以写为 $ψ_i \sim (δn^f_i+\frac{1}{2})^{-1} f_i$。 $ψ$ 和局部矩 $ψ'$ 之间的新兴近藤耦合 $J_K \sim U$（$U$ 是局部哈伯德相互作用）将莫特转变框架为近藤屏蔽转变，并通过扭转角 $θ$ 进行调整。远离魔角，近藤筛选的重半金属在 $T_K$（近藤温度）以下发展，$Z$ 消失。引入反亨德耦合 $J_A$ 即使在 $ν=0$ 时也会在莫特边界附近产生完全带隙或向列型、节点带隙的 s 波超导穹顶。 在其他整数填充 $ν= \pm 1, \pm 2$ 时，增加带宽首先将小能隙莫特态驱动为中间二次能带接触半金属，然后进入具有大费米表面的重费米液体。我们的结果为新兴的重费米子物理建立了一个统一的框架，其中包括来自 $f$ 轨道的巡回载流子和局部矩。
**讨论重点：** 在这里，我们展示了在整数填充时扭曲双层石墨烯（TBG）中出现的类似现象，并且可以通过投影有源带限制内的新兴重费米子框架捕获。与包含远程带的模型不同，我们有效的重费米子描述来自于 \textit{混合价莫特} 物理通过解耦电荷和局部矩扇区。 结合关键词看，阅读时应重点关注重费米子相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 6. Lectures on ultrathin film ferromagnetism

- Source: arXiv
- Date: 2026-08-12T15:46:08Z
- Venue: cond-mat.mes-hall
- Authors: D. Pescia
- Link: https://arxiv.org/abs/2608.12189v1
- Score: 18.0
- Match: 标题匹配 ferromagnetism; 最近 3 天发布

**中文摘要：** 在这些讲义中，我们回顾了由 3d 过渡金属覆盖层组成的超薄膜铁磁性研究中得出的一些基本原理。他们的成长往往是一层一层的。这种生长模式沿垂直方向产生量子阱，深刻影响材料的任何物理特性。此外，垂直限制建立了自旋系综，该系综沿着面内方向延伸到宏观距离，并且沿着垂直（垂直）方向是有限的，即它们是二维的。 因此，它们表现出源自二维的基态特性，例如“死”磁层或“增强磁矩”、振荡层间磁耦合以及反常的垂直与面内磁各向异性，在某些特定情况下，会产生自旋的垂直集体方向。在有限温度下，观察到铁磁序持续存在，并且根据重正化群对超薄膜的磁序进行分析为解释这一观察提供了合适的框架。 正如对临界点附近数据的精确分析所示，铁磁序在相变时丢失，该相变紧随二维伊辛普适性类。垂直自旋方向经常被观察到通过重新取向相变而在平面内转动，这也可以通过重正化群论证来正确描述。最后，垂直自旋方向引入了铁磁序的拓扑激发，由反向垂直自旋方向的条纹组成。 条带顺序经历了向顺磁态的相变，这一点尚未完全被理解。
**讨论重点：** 在有限温度下，观察到铁磁序持续存在，并且根据重正化群对超薄膜的磁序进行分析为解释这一观察提供了合适的框架。他们的成长往往是一层一层的。 结合关键词看，阅读时应重点关注铁磁性相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 7. Spin-polarized supercurrents and Josephson diode effect in altermagnets

- Source: arXiv
- Date: 2026-08-12T10:33:33Z
- Venue: cond-mat.supr-con, cond-mat.mes-hall
- Authors: Janus F. Niebuhr, Matthias Eschrig, Danilo Nikolić
- Link: https://arxiv.org/abs/2608.11906v1
- Score: 18.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们对由放置在两个 BCS 超导体 (SC) 之间的 d 波交流磁体 (AM) 组成的结点中的约瑟夫森效应进行了系统的理论研究。一般来说，SC/AM 界面是自旋活性的，并通过自旋相关的 $δ$ 势进行建模，允许局部交换场矢量的任意方向。 该模型是在全量子 (Gor'kov) 和准经典 (Eilenberger) 格林函数技术内制定的，应用于两种不同的情况：(i) 弱自旋极化 AM（交换场与费米能量相比小得多）和 (ii) 强自旋极化 AM（交换场与费米能量相当）。我们将我们的模型应用于 SC/AM/SC 几何结构，考虑约瑟夫森电流相位关系 (CPR)。在弱自旋极化状态下，CPR 显示出正常的约瑟夫森效应。 无论交变磁体的方向如何，结点都会经历 $0-π$ 转变。根据方向，系统显示类似于铁磁或反铁磁结的特征。为了研究自旋极化电流和非互易输运作为当前工作的核心结果，我们将主要焦点放在强自旋极化状态上。在这个制度下，我们区分两种情况。 跨结点的共面交换场轮廓显示了正常的约瑟夫森效应；然而，CPR 中具有纯净且稳定的长程二次谐波。相比之下，非共面交换场分布会在结处产生所谓的量子几何相位，从而导致约瑟夫森 CPR 中不存在相转化中心。结果，出现了约瑟夫森二极管效应，其充电二极管效率显着高于 30%，完美的自旋二极管效率为 100%。
**讨论重点：** 我们对由放置在两个 BCS 超导体 (SC) 之间的 d 波交流磁体 (AM) 组成的结点中的约瑟夫森效应进行了系统的理论研究。该模型是在全量子 (Gor'kov) 和准经典 (Eilenberger) 格林函数技术内制定的，应用于两种不同的情况：(i) 弱自旋极化 AM（交换场与费米能量相比小得多）和 (ii) 强自旋极化 AM（交换场与费米能量相当）。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 8. Geometry of Noisy Quantum Many-Body Dynamics with Continuous Symmetries: Entanglement and Correlations

- Source: arXiv
- Date: 2026-08-11T18:00:01Z
- Venue: cond-mat.stat-mech, cond-mat.str-el, hep-th
- Authors: Marco Lastres, Sanjay Moudgalya
- Link: https://arxiv.org/abs/2608.11297v1
- Score: 17.0
- Match: 标题匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 我们研究具有全局连续对称性的噪声布朗模型中的酉量子动力学，例如 $U(1)$ 和 $SU(2)$，重点关注 Rényi 纠缠熵以及流体动力学和非流体动力学相关器。通过将平均后期动力学映射到有效复制哈密顿量的低能物理，我们发现演化是由其基态流形的量子几何控制的，这与$k$交换子的几何形状——系统的$k$复制的对称代数直接相关。 在交互系统中，这些 $k$-交换子通常仅由系统的对称性决定，与噪声演化的微观细节无关。这使我们能够使用瞬态变分原理（TDVP）为具有连续对称性的相互作用系统中的亚弹道Rényi纠缠增长和非流体动力相关器的异常衰变提供简单的几何解释。 我们发现这种行为与 $k$ 交换流形内的奇点密切相关，这些奇点源自希尔伯特空间中由于连续现场对称性而存在的冻结“空”状态。这也揭开了空洞在这些可观测量动力学中的重要作用的神秘面纱，这些可观测量先前在 $U(1)$ 对称系统中被确定。我们比较了具有阿贝尔和非阿贝尔连续对称性的相互作用系统以及自由费米子系统中的这些行为，这些系统的 $k$-交换子的几何形状不同。 最终，这项工作为系统地研究具有连续对称性的噪声系统（包括哈尔随机电路）中的可观测量提供了一个通用的几何框架。
**讨论重点：** 我们研究具有全局连续对称性的噪声布朗模型中的酉量子动力学，例如 $U(1)$ 和 $SU(2)$，重点关注 Rényi 纠缠熵以及流体动力学和非流体动力学相关器。最终，这项工作为系统地研究具有连续对称性的噪声系统（包括哈尔随机电路）中的可观测量提供了一个通用的几何框架。 结合关键词看，阅读时应重点关注量子多体相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Floquet Engineering of Topological Phases and Magneto-Optical Response in a Driven $d$-wave Altermagnet

- Source: arXiv
- Date: 2026-08-11T17:51:05Z
- Venue: cond-mat.mes-hall
- Authors: Muzamil Shah
- Link: https://arxiv.org/abs/2608.11192v1
- Score: 17.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究了 Floquet 线性偏振光驱动如何控制二维 (2D) $d$ 波交变磁体的拓扑和磁光响应。在没有线性偏振光场和自旋守恒的情况下，我们发现该系统具有自旋陈（量子自旋霍尔模拟）相，两个自旋扇区中的陈数具有相反的符号。照射光场打破了自旋扇区之间的 $C_{4z}\mathcal{T}$ 晶体反统一对称性。 对称性破缺源自偏振相关的 Peierls 相，它沿两个轴各向异性地重新规范化跳跃。由此产生的自旋选择性间隙闭合产生中间陈绝缘相 $C=\pm1$。驱动幅度 $A_0$ 决定反转阈值，而将偏振旋转 $π/2$ 会交换自旋扇区并反转陈数。使用久保形式主义，我们计算了频率相关的纵向电导率和霍尔电导率，并导出了独立式导电片的相应法拉第和克尔旋转。 纵向响应跟踪 Floquet 重整化带间阈值，而光学霍尔响应与磁光旋转的符号一起区分两个相反的贝里曲率手性。相当大的克尔角仅出现在狭窄的共振窗口内，并且应与反射强度和克尔椭圆率一起解释。这些结果表明，线偏振光可作为 d$ 波交替磁体中自旋分辨能带反转、陈数转换和非接触式光学检测的对称选择手柄。
**讨论重点：** 我们研究了 Floquet 线性偏振光驱动如何控制二维 (2D) $d$ 波交变磁体的拓扑和磁光响应。在没有线性偏振光场和自旋守恒的情况下，我们发现该系统具有自旋陈（量子自旋霍尔模拟）相，两个自旋扇区中的陈数具有相反的符号。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 10. Quantum Mechanism of Piezomagnetism in Higher-Spin Altermagnets

- Source: arXiv
- Date: 2026-08-11T09:54:41Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Daisuke Yamamoto, Makoto Naka
- Link: https://arxiv.org/abs/2608.10735v1
- Score: 17.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们使用风味波方法研究具有易平面单离子各向异性的高自旋交变磁体中的压磁性。我们表明，高自旋集体模式的量子涨落提供了压磁响应的微观起源。对于整数自旋，相关分支在接近大$D$转变时软化并演变成类希格斯振幅模式，赋予激发相当大的偶极分量并产生压磁性的显着增强。 相比之下，在半整数系统中，随着各向异性的增加，高自旋分支逐渐与低能偶极扇区分离，这抑制了它们对响应的贡献。这种整数-半整数对比将宏观压磁性与多极激发的低能命运直接联系起来。我们的结果将压磁学确立为高自旋量子动力学的探针，并将高自旋交变磁体确定为量子磁弹性响应的有希望的设置。
**讨论重点：** 我们使用风味波方法研究具有易平面单离子各向异性的高自旋交变磁体中的压磁性。我们表明，高自旋集体模式的量子涨落提供了压磁响应的微观起源。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
