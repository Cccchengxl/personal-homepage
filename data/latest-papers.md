# Latest papers for 程旭丽

Updated: 2026-08-28T08:39:14.490914+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: HTTP Error 429: Unknown Error
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: HTTP Error 429: Unknown Error
- 凝聚态物理强关联体系和多铁性质 returned 1 papers; target range is 5-10.

## 机器学习分子动力学模拟与热力学性质

### 1. Comparative Assessment of Thermal Transport Theories: Dual-Channel Mechanism Dictates Heat Transport in Ultralow-$κ$ Materials

- Source: arXiv
- Date: 2026-08-22T00:04:18Z
- Venue: cond-mat.mtrl-sci
- Authors: Soham Mandal, Ashutosh Srivastava, Tanmoy Das, Manish Jain, Abhishek Kumar Singh, Prabal K. Maiti
- Link: https://arxiv.org/abs/2608.21695v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 强非谐晶体固体中的反常热传输既对理论理解提出了根本性挑战，也为热电和热障涂层应用提供了机会。尽管格林-久保理论再现了高温下的实验热导率（$κ$），但它缺乏微观洞察力并且忽略了晶格振动的玻色-爱因斯坦统计。另一方面，基于声子气体图的传统玻尔兹曼输运方程（BTE）框架由于强非谐性引起的过阻尼声子而失败。 在此，通过机器学习原子间势并采用维格纳输运方程 (WTE) 框架，通过明确解释温度依赖性晶格动力学，研究了金属硫族化物 TlAgSe 和全无机层状 Ruddlesden-Popper 钙钛矿 Cs$_2$PbI$_2$C$_2$ 的热输运特性。 至关重要的是，热传导不仅受 BTE 内描述的高阶声子散射主导群体的传输通道控制，而且还受 WTE 框架中由本征态之间波状分支间相干性产生的相干通道控制。结合四声子散射，WTE 预测平均室温 $κ$ 值为 0.31 Wm$^{-1}$K$^{-1}$ (TlAgSe) 和 0.38 Wm$^{-1}$K$^{-1}$ (Cs$_2$PbI$_2$C$_2$)，与实验非常吻合。 声子散射率分析揭示了强相干性的贡献和普遍的过阻尼声子模式，证明了基于仅具有一阶非谐扰动的声子准粒子图的传统 BTE 框架的崩溃。这种计算方法提供了超低κ$材料中热传输的统一描述，为声子和热电器件的合理设计提供了基础。
**讨论重点：** 这种计算方法提供了超低κ$材料中热传输的统一描述，为声子和热电器件的合理设计提供了基础。另一方面，基于声子气体图的传统玻尔兹曼输运方程（BTE）框架由于强非谐性引起的过阻尼声子而失败。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids

- Source: arXiv
- Date: 2026-08-21T20:46:16Z
- Venue: cond-mat.mtrl-sci
- Authors: Gavin Winter, Juno Nam, Rafael Gómez-Bombarelli
- Link: https://arxiv.org/abs/2608.21624v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 从分子动力学 (MD) 模拟中预测移动离子自扩散率 $D^*$ 对于识别有前途的固态电解质至关重要，但直接模拟离子扩散的计算成本很高，特别是对于高精度机器学习原子间势 (MLIP)。扩散是一个缓慢的、突发的过程，需要很长的轨迹才能收敛。 相比之下，热力学性质收敛得更快：焓 $h$、振动熵 $s_{vib}$ 和 2 体、过量构型熵 $s^{ex}_{2,config}$ 可以从相对较短的 MD 轨迹中提取，并且它们编码有关自由能景观的丰富信息，最终产生自扩散性等输运性质。讨论了这些热力学性质和离子扩散之间的直观相关性，激发了数据驱动的方法来利用这种联系。 训练一个简单的神经网络，根据短 MD 轨迹计算的特征来预测扩散率：振动指纹（振动态密度，VDOS）和结构指纹（径向分布函数，RDF），以 MLIP 嵌入中编码的化学信息为条件。这种组合允许模型预测收敛的 $\log_{10} D^*$ (cm$^2$/s) \textemdash\，通常是从明显更长的 MD 模拟 \textemdash\ 获得的，平均绝对误差为 0.398，Spearman 等级相关性 $ρ$ 为 0.844。
**讨论重点：** 讨论了这些热力学性质和离子扩散之间的直观相关性，激发了数据驱动的方法来利用这种联系。扩散是一个缓慢的、突发的过程，需要很长的轨迹才能收敛。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 3. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 10.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 然而，多组件批量 MD 模拟仍然难以实现，因为现有 MLIP 的 HBM 足迹（对于单组件系统来说已经很大）在多组件场景中呈爆炸性增长。本文提出了一种 HBM 占用空间较小的 MLIP（不到现有 MLIP 的 3%），仅使用数百个 GPU 即可解锁多组件批量 MD。这是通过首先将特征向量和中间张量识别为现有 MLIP 中 HBM 足迹的两个主要贡献者来实现的。 为了解决这两个来源，通过引入物理和化学知识来降低特征向量的维数，并通过积极地将所有内核融合到单个巨型内核中来消除中间张量。在评估中，所提出的MLIP使用了144个NVIDIA A100 GPU对具有1.14x10^9原子的6分量体系统进行MD模拟，而此前这种MD模拟空间尺度仅限于一元系统，通常在配备数万个GPU的高端超级计算机上实现。
**讨论重点：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 4. Machine Learning Guided Discovery of Corundum High Entropy Oxides

- Source: arXiv
- Date: 2026-08-20T22:21:15Z
- Venue: cond-mat.mtrl-sci
- Authors: Abraham A. Mancilla, Oliver A. Dicks, Solveig S. Aamlid, Mario Ulises González-Rivas, Karl Tsang, Dongjoon Song
- Link: https://arxiv.org/abs/2608.20596v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 高熵氧化物（HEO）领域的早期思考强调了它们可能的丰富性，并通过组合论证暗示了无数新材料的存在。事实证明，实验现实更具挑战性：仅根据离子半径、晶格几何形状和电荷平衡考虑因素，无法直接预测 HEO 的稳定性。在这项工作中，我们利用机器学习原子间势 (MLIP) 来预测从一系列三价阳离子衍生的 $A_2$O$_3$ 形式的 HEO 的合成性。 从近 500 种可能的成分中，我们确定了 16 种有前途的候选成分，用于固态和燃烧合成的实验验证。我们在刚玉结构中发现了三种新的 HEO，包括 (Al,Cr,Fe,Rh,Sc)$_2$O$_3$，以及一种新型阳离子有序相，(Al,Fe,Ga,Sc)$_2$O$_3$。到目前为止，最常见的合成结果是竞争相的混合物，有时涉及氧化还原反应。 我们的结果还揭示了最终产品对合成方法的深刻依赖性，其中两种合成方法之间的定性等效结果仅在 16 种测试组合物中的 3 种中观察到。我们得出的结论是，HEO 的出现率比最初认为的要少得多，机器学习方法可以有效地引导我们找到“大海捞针”。
**讨论重点：** 我们的结果还揭示了最终产品对合成方法的深刻依赖性，其中两种合成方法之间的定性等效结果仅在 16 种测试组合物中的 3 种中观察到。事实证明，实验现实更具挑战性：仅根据离子半径、晶格几何形状和电荷平衡考虑因素，无法直接预测 HEO 的稳定性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释。

### 5. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样化的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议，在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 7. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 8. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序，即我们称为删除的方法，它比一系列替代提取方法具有优越的性能。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相由强电子声子耦合和伴随的晶格不稳定性产生。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，揭示了优先剪切路径，为变形和孪晶机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

## 凝聚态物理强关联体系和多铁性质

### 1. Efficient quantum implementation of dynamical mean field theory for correlated materials

- Source: Journal
- Date: 2026-08-17
- Venue: npj Computational Materials
- Authors: Norman Hogan, Efekan Kökcü, Thomas Steckmann, Liam P. Doak, Carlos Mejuto-Zaera, Daan Camps
- Link: https://doi.org/10.1038/s41524-026-02289-2
- Score: 7.0
- Match: 标题匹配 dynamical mean field theory; 近两周发布

**中文摘要：** 当前元数据未提供原文摘要。论文题目为“Efficient quantum implementation of dynamical mean field theory for correlated materials”。
**讨论重点：** 结合关键词看，阅读时应重点关注动力学平均场理论相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。
