# Latest papers for 程旭丽

Updated: 2026-08-19T01:00:26.547027+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 17.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 然而，多组件批量 MD 模拟仍然难以实现，因为现有 MLIP 的 HBM 足迹（对于单组件系统来说已经很大）在多组件场景中呈爆炸性增长。本文提出了一种 HBM 占用空间较小的 MLIP（不到现有 MLIP 的 3%），仅使用数百个 GPU 即可解锁多组件批量 MD。这是通过首先将特征向量和中间张量识别为现有 MLIP 中 HBM 足迹的两个主要贡献者来实现的。 为了解决这两个来源，通过引入物理和化学知识来降低特征向量的维数，并通过积极地将所有内核融合到单个巨型内核中来消除中间张量。在评估中，所提出的MLIP使用了144个NVIDIA A100 GPU在具有1.14x10^9原子的6分量体系统上执行MD模拟，而此前这种MD模拟空间尺度仅限于一元系统，并且通常在配备数万个GPU的高端超级计算机上实现。
**讨论重点：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training

- Source: arXiv
- Date: 2026-08-17T11:15:35Z
- Venue: physics.chem-ph, physics.atom-ph
- Authors: Marie Bluntzer, Jules Tilly, Christoph Brunken
- Link: https://arxiv.org/abs/2608.16418v1
- Score: 13.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 训练集的质量和多样性是机器学习原子间势 (MLIP) 可靠性的关键决定因素，但完整使用大量数据集通常是不切实际且多余的，因此智能数据选择至关重要。然而，一个主要瓶颈是缺乏用于统一访问、整理和二次采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面差异很大。 我们使用 ChemReporter 解决了这一差距，这是一个与方法无关的模块化框架，可将任意分子和材料数据集转换为统一的、可查询的表示形式，并将结果直接导出到 MLIP 就绪的训练数据中。 ChemReporter 分三个解耦阶段运行：处理，将原始数据集解析为分区的 Apache Parquet 存储库，其中包含结构、物理和化学元数据；查询，通过 CLI 或 Python API 使用任意选择标准（从简单的物理约束到自定义的用户定义策略）过滤和采样此存储库；导出，将选定的子集流式传输到 HDF5 文件中，以便直接在现代 MLIP 训练框架中使用。 在整个过程中，每个导出的数据点都可以追溯到其原始源条目，并且在相同的配置和查询数据库版本的情况下，可以可靠地再现数据集导出。由于数据以可查询、磁盘支持的格式存储，ChemReporter 可以处理远远大于可用内存的数据集，从而使其能够在标准计算基础设施上扩展到数十亿结构的数据集。 ChemReporter 可在 GitHub 和 PyPI 上使用 Apache License 2.0。
**讨论重点：** 我们使用 ChemReporter 解决了这一差距，这是一个与方法无关的模块化框架，可将任意分子和材料数据集转换为统一的、可查询的表示形式，并将结果直接导出到 MLIP 就绪的训练数据中。然而，一个主要瓶颈是缺乏用于统一访问、整理和二次采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面差异很大。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Electrostatic Phenomenology Benchmarks for Machine-Learned Interatomic Potentials in Electrochemistry: Beyond the Energy-Force Metric

- Source: arXiv
- Date: 2026-08-14T10:03:18Z
- Venue: cond-mat.mtrl-sci, physics.chem-ph, physics.comp-ph
- Authors: Barbara Sumić, Ria Vasdev, Sudheesh Kumar Ethirajan, Jing Yang, Clotilde S. Cucinotta, Richard G. Hennig
- Link: https://arxiv.org/abs/2608.14153v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 准确处理机器学习原子间势 (MLIP) 中的长程相互作用对于电化学模拟至关重要。然而，仅靠总能量和力误差不足以确定 MLIP 的物理精度，因为它们无法检测模型中的定性不一致，例如图像电荷吸引、介电屏蔽或电荷转移的预测。我们引入了一个基准套件 EPhEct（电化学静电现象），其中包含专门的测试用例，旨在评估电化学相关物理现象的 MLIP。 该测试探测金属电极处的图像电荷吸引力、作为离子和电子屏蔽探针的纵向和横向光学声子之间的分裂、界面水的偶极矩以及离子放电期间的费米能级钉扎。这些测试建立了一个定性诊断程序，作为总体能量指标的补充。
**讨论重点：** 我们引入了一个基准套件 EPhEct（电化学静电现象），其中包含专门的测试用例，旨在评估电化学相关物理现象的 MLIP。然而，仅靠总能量和力误差不足以确定 MLIP 的物理精度，因为它们无法检测模型中的定性不一致，例如图像电荷吸引、介电屏蔽或电荷转移的预测。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Evaluating Electrostatic Embedding MLIP/MM for Relative Binding Free Energy Calculations

- Source: arXiv
- Date: 2026-08-13T15:19:17Z
- Venue: physics.chem-ph, physics.comp-ph
- Authors: Stephen E. Farr, Gianni De Fabritiis
- Link: https://arxiv.org/abs/2608.13355v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 炼金术相对结合自由能 (RBFE) 计算受到经典力场的固定电荷近似的限制。混合机器学习原子间势/分子力学 (MLIP/MM) 方案可以纠正配体应变，但在机械嵌入下仍然描述具有静点电荷的配体-环境静电。已经提出了将机器学习的电荷耦合到 MM 环境的静电嵌入方案，并针对简单系统的 QM/MM 进行了验证，但尚未在生产炼金工作流程中进行测试。 我们采用 Semelak 等人的静电嵌入方案，并在蛋白质-配体 RBFE 上对其进行评估。我们在 AceFF 数据集中的 $10^{6}$ 构象上训练了一个 TensorNet2 模型 \texttt{AceFF-2-RESP-1}，联合预测能量、力和约束静电势 (RESP) 电荷。我们选择 RESP 而不是 MBIS，是因为它与所耦合的 AMBER 系列力场具有可通约性。预测的电荷进入粒子网格 Ewald 和的短程直接空间部分，并使用 Thole 阻尼来防止炼金术变换期间发生极化灾难。 我们在 Wang 等人基准集中的五个目标上测试了该方案，这些目标由先前的研究提前确定，每个边缘和匹配的协议具有三个重复。静电嵌入提高了 TYK2 的每项准确性和相关性指标（$ΔΔG$ RMSE $0.86 \rightarrow 0.45$~kcal/mol 相对于 GAFF2），但与 CDK2、凝血酶、p38 和 JNK1 的经典和机械嵌入基线相当。标准的单分子能量和电荷基准并不能很好地预测这种目标依赖性结果。 TYK2 在薛定谔基准测试中将良好的 $ΔΔG$ 精度与最低的力误差结合在一起，但这种模式并不适用于其他目标。
**讨论重点：** 我们在 Wang 等人基准集中的五个目标上测试了该方案，这些目标由先前的研究提前确定，每个边缘和匹配的协议具有三个重复。我们在 AceFF 数据集中的 $10^{6}$ 构象上训练了一个 TensorNet2 模型 \texttt{AceFF-2-RESP-1}，联合预测能量、力和约束静电势 (RESP) 电荷。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
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

**中文摘要：** 为了通过原子模拟（例如分子动力学（MD））适当捕获大规模材料特征和突发现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 为了计算感兴趣区域中原子上的 DFT 力，例如用于原子间势的主动学习或动态训练，需要从较大的模拟框中提取一小组原子，并且通常使用 DFT 的周期性边界条件。然而，尚未系统地分析选择这组提取的原子的形状和大小以及生成潜在必要的钝化包络的方法。 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。我们使用多种材料系统进行测试，其中包括无定形 $\mathrm{SiO_2}$、具有螺旋位错的 Ta 和熔融 C。我们演示了一种非常简单的程序（我们称为删除的方法），其性能优于一系列替代提取方法。
**讨论重点：** 在这项工作中，我们对多种技术进行了基准测试，包括基于生成扩散的人工智能 (AI) 方法，用于从大型体配置中提取原子环境，并将其嵌入到适合具有周期性边界条件的 DFT 计算的较小配置中。然而，驱动这些模拟的力场模型通常使用密度泛函理论 (DFT) 参考数据进行训练，仅限于数百或数千个原子数量级的相对较小的配置。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 1T 过渡金属二硫属化物中的电荷密度波 (CDW) 相是由强电子声子耦合和伴随的晶格不稳定性产生的。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学 (MD) 捕获其随温度变化的结构演化仍然具有挑战性。 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。针对 DFT 位移能量的基准测试确定了 UMA-s-1p1 通用机器学习潜力，具有足够的精度用于后续的有限温度模拟。 我们的结果表明，大规模 MD 模拟再现了实验观察到的从低温大卫之星 (SoD) 扭曲结构到高温原始六边形结构的相变序列，通过归因于 SoD 的 Ta 原子数量来量化。加热-冷却循环表现出热滞后，并且在冷却时，系统冻结成多域状态，其中α和\b{eta} CDW手性独立成核并持续到最低温度。 这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论 (DFT)、通用机器学习原子间势 (MLIP)、MD 和温度相关的有效势声子计算来研究单层 1T-TaS2 中 CDW 跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用 MLIP 可以为 CDW 材料的有限温度研究提供可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，并揭示了优先剪切路径，为变形和孪生机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

## 凝聚态物理强关联体系和多铁性质

### 1. Antiferroquadrupolar Order in Altermagnetic CoF$_2$

- Source: arXiv
- Date: 2026-08-14T20:56:18Z
- Venue: cond-mat.str-el
- Authors: Daniel Halliday, Laura Pöysti, Chung Xu, Daniel A. Mayoh, Didier Wermeille, Dharmalingam Prabhakaran
- Link: https://arxiv.org/abs/2608.14889v1
- Score: 27.0
- Match: 摘要匹配 ferromagnetism; 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet

**中文摘要：** 交替磁体具有非相对论性自旋分裂电子​​态，其微观起源理论上与隐藏的电荷顺序相关，但对该电荷顺序的实验研究有限。因此，我们研究了 CoF$_2$ 内的电荷顺序，CoF$_2$ 是一种具有金红石晶体结构和 $Γ$ 点反铁磁性的 $d$ 波交变磁化合物。结合共振弹性X射线散射、对称性分析和从头计算，我们直接观察到电荷排序并将其识别为反铁四极性质。 通过电子结构计算，我们表明，实验观察到的反铁四极序引起了特征性的交变磁自旋分裂，从而为交变磁序参数分解为磁自由度和电荷自由度建立了经验证据。因此，我们证明反铁四极有序是 CoF$_2$ 交变磁性的微观起源，对更广泛的金红石交变磁体家族具有影响。 此外，我们的方法适用于研究一般的交变磁性，已经证明共振弹性 X 射线散射可以作为支撑这些材料中自旋分裂电子​​态的电荷多极子的直接探针。
**讨论重点：** 因此，我们研究了 CoF$_2$ 内的电荷顺序，CoF$_2$ 是一种具有金红石晶体结构和 $Γ$ 点反铁磁性的 $d$ 波交变磁化合物。此外，我们的方法适用于研究一般的交变磁性，已经证明共振弹性 X 射线散射可以作为支撑这些材料中自旋分裂电子​​态的电荷多极子的直接探针。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Electrically Switchable Spintronics in a Multiferroic Altermagnet

- Source: arXiv
- Date: 2026-08-16T22:54:37Z
- Venue: cond-mat.mes-hall
- Authors: Martin Latorre
- Link: https://arxiv.org/abs/2608.15953v1
- Score: 26.0
- Match: 标题匹配 multiferroic; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们引入了二维晶格的最小模型，该模型在自发对称性破缺时，同时产生交变磁序、有限电极化和自旋极化输运响应，所有这些都由外部电场控制。通过将二聚交变磁体耦合到外部电场，我们表明这三个阶参数不仅是兼容的，而且是动态纠缠的，因此切换一个参数（例如，用电场反转极化）必然会重新配置其他两个参数。 我们证明，该模型为设计下一代自旋电子逻辑和纯自旋电流MEMS器件提供了清晰的物理蓝图，将补偿磁体的超快、无杂散场的优点与铁电体的低功耗开关架构相结合。
**讨论重点：** 我们引入了二维晶格的最小模型，该模型在自发对称性破缺时，同时产生交变磁序、有限电极化和自旋极化输运响应，所有这些都由外部电场控制。通过将二聚交变磁体耦合到外部电场，我们表明这三个阶参数不仅是兼容的，而且是动态纠缠的，因此切换一个参数（例如，用电场反转极化）必然会重新配置其他两个参数。 结合关键词看，阅读时应重点关注多铁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Strain-stabilized altermagnetism and conductivity anisotropy in FeSb2

- Source: arXiv
- Date: 2026-08-16T16:18:25Z
- Venue: cond-mat.mtrl-sci
- Authors: Masoumeh Davoudiniya, Alyssa M. Kennedy, Amy Y. Liu, Gen Yin
- Link: https://arxiv.org/abs/2608.15839v1
- Score: 26.0
- Match: 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们表明，当施加拉伸应变时，FeSb2 会经历从传统反铁磁体到交变磁体的转变。在交变磁相中，即使没有自旋轨道耦合，克莱默简并度的提升也会导致费米能级附近的自旋分裂高达~0.2eV。向交变磁相的转变伴随着费米表面几何形状的巨大变化，这导致单轴电导率各向异性高达~60%，远大于在典型铁磁金属中观察到的电导率各向异性。 利用密度泛函理论和万尼尔插值费米面，我们表明这种磁输运行为可以作为向交变磁相转变的实验指标。这些发现凸显了 FeSb2 作为一种多功能、应变可调的平台，可用于探索和利用自旋电子器件的交变磁输运现象。
**讨论重点：** 我们表明，当施加拉伸应变时，FeSb2 会经历从传统反铁磁体到交变磁体的转变。在交变磁相中，即使没有自旋轨道耦合，克莱默简并度的提升也会导致费米能级附近的自旋分裂高达~0.2eV。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Chiral spin liquid and chiral antiferromagnetism in half-filled moiré Hubbard model: possible applications to twisted bilayer TMDs

- Source: arXiv
- Date: 2026-08-14T17:17:33Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Chuyi Tuo, Hong Yao
- Link: https://arxiv.org/abs/2608.14503v1
- Score: 24.0
- Match: 标题匹配 Hubbard model; 摘要匹配 density matrix renormalization group; 标题匹配 ferromagnetism; 近两周发布

**中文摘要：** 扭曲的过渡金属二硫化物提供了一个异常可调的莫尔条纹平台，用于研究传统凝聚态系统之外的相关物理。特别是，位移场和扭转角之间有趣的相互作用仍有待完全解决。在本文中，我们使用大规模密度矩阵重整化群模拟来研究半填充时三角晶格上的最小莫尔哈伯德模型，其中位移场效应由自旋相关的交错通量捕获。 我们发现位移场在几个定性方面显着丰富了三角哈伯德相图。它迅速使手性自旋液相超出狭窄的弱场范围，在强耦合$120^\circ$反铁磁相中引起明显的手性相关性，并在较弱的耦合下稳定不相称的自旋密度波相位。我们进一步发现了有限位移场下手性自旋液体和手性反铁磁相之间连续转变的特征，这可能是由自旋凝聚驱动的。 我们的结果揭示了丰富的位移场驱动的多体物理，并为莫尔超晶格系统的未来实验提供了有用的指导。
**讨论重点：** 在本文中，我们使用大规模密度矩阵重整化群模拟来研究半填充时三角晶格上的最小莫尔哈伯德模型，其中位移场效应由自旋相关的交错通量捕获。特别是，位移场和扭转角之间有趣的相互作用仍有待完全解决。 结合关键词看，阅读时应重点关注Hubbard 模型、密度矩阵重整化群、铁磁性相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Topological Altermagnetic Insulators

- Source: arXiv
- Date: 2026-08-16T15:38:43Z
- Venue: cond-mat.str-el
- Authors: Jasmin Bedow, Nitin Kaushal, Marcel Franz
- Link: https://arxiv.org/abs/2608.15811v1
- Score: 23.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究了相关交变磁体的原型利布晶格模型中伊辛自旋轨道耦合稳定的交变拓扑相的出现。通过处理 Hartree-Fock 内的电子相互作用和精确的对角化技术，我们在参数空间的广阔区域内建立了量子自旋霍尔效应与交变自旋序的共存，每个晶胞的平均电子密度为 2 和 4。 我们探索沿边缘的磁性结构如何影响相关拓扑边缘模式的电子行为，证明它们对反演对称破缺项的鲁棒性。
**讨论重点：** 我们研究了相关交变磁体的原型利布晶格模型中伊辛自旋轨道耦合稳定的交变拓扑相的出现。通过处理 Hartree-Fock 内的电子相互作用和精确的对角化技术，我们在参数空间的广阔区域内建立了量子自旋霍尔效应与交变自旋序的共存，每个晶胞的平均电子密度为 2 和 4。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Design of altermagnetism in oxide superlattices exploiting interface effects and quantum confinement

- Source: arXiv
- Date: 2026-08-16T14:34:24Z
- Venue: cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Subhadeep Bandyopadhyay, Rossitza Pentcheva
- Link: https://arxiv.org/abs/2608.15765v1
- Score: 23.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁性的发现引发了深入的研究，并为自旋电子和传输应用开辟了新的途径。虽然目前的努力主要集中在通常是绝缘的块体材料上，但在这里我们提出了通过利用对称性破缺、静电掺杂和限制来实现氧化物超晶格中交变磁性和金属性的组合的设计策略。 虽然块状 SrCrO3 由于相邻层之间的补偿效应而不会表现出交变磁性，但我们使用 Hubbard U 参数进行的密度泛函理论计算表明，限制在 (SrCrO3)1/(SrTiO3)1(001) 超晶格 (SL) 中的单个 SrCrO3 层表现出相当大的非相对论自旋分裂 (NRSS)，高达 350 meV，具有块状 d 波性质，这是由于轨道排序和八面体旋转（OOR）的共存。由于该系统是绝缘的，我们扩展到 SrCrO3/LaCrO3(001) SL。 在 (SrCrO3)4/(LaCrO3)4(001) SL 中，界面处的极性不连续性和更强的 OOR 的结合促进了金属 d 波交变磁性。高达 120 meV 的 NRSS 由费米能级的界面 Cr d 带贡献，表明存在自旋选择性费米表面嵌套。这些发现确立了氧化物超晶格作为实现和探索量子传输和自旋电子功能的交变磁性的有前途的平台
**讨论重点：** 虽然目前的努力主要集中在通常是绝缘的块体材料上，但在这里我们提出了通过利用对称性破缺、静电掺杂和限制来实现氧化物超晶格中交变磁性和金属性的组合的设计策略。这些发现确立了氧化物超晶格作为实现和探索量子传输和自旋电子功能的交变磁性的有前途的平台 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Surface weak ferromagnetism

- Source: arXiv
- Date: 2026-08-17T17:02:29Z
- Venue: cond-mat.mes-hall
- Authors: Vladimir A. Zyuzin
- Link: https://arxiv.org/abs/2608.16808v1
- Score: 17.0
- Match: 标题匹配 ferromagnetism; 最近 3 天发布

**中文摘要：** 本文提出了一种尼尔有序反铁磁体模型，该模型表现出仅限于晶体表面的弱铁磁矩，该铁磁矩是由破缺表面对称性引起的自旋轨道耦合产生的。根据晶体终端，表面磁矩可以与顶部和底部表面上相同或相反的符号对齐，从而在后一种配置的反射时产生零法拉第效应与有限克尔效应。
**讨论重点：** 本文提出了一种尼尔有序反铁磁体模型，该模型表现出仅限于晶体表面的弱铁磁矩，该铁磁矩是由破缺表面对称性引起的自旋轨道耦合产生的。根据晶体终端，表面磁矩可以与顶部和底部表面上相同或相反的符号对齐，从而在后一种配置的反射时产生零法拉第效应与有限克尔效应。 结合关键词看，阅读时应重点关注铁磁性相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 8. Optical Response Beyond Magnetic Symmetries

- Source: arXiv
- Date: 2026-08-17T10:19:10Z
- Venue: cond-mat.mtrl-sci
- Authors: Javier Sivianes, Enrique Boquete-Someso, Daniel Hernangómez-Pérez, Julen Ibañez-Azpiroz
- Link: https://arxiv.org/abs/2608.16368v1
- Score: 16.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 磁性材料的光学响应通常通过磁性空间群（MSG）进行分类，其中自旋和晶格通过相对论自旋轨道相互作用锁定。然而，大多数光学可观测量主要受非相对论物理学控制，因此纯粹基于 MSG 的描述可能会忽略重要的见解。在这里，我们系统地展示了在非相对论水平上运行的自旋空间群（SSG）为分析磁体的各种光学响应提供了更广泛和更具预测性的框架。 着眼于线性光学吸收，我们推导了 SSG 施加的变换规则，并表明它们生成有效的实空间点群，这可以加强电荷响应系数之间的关系，而传统 MSG 分析中没有这种关系。我们阐述了具有可调谐自旋轨道耦合的利布晶格交变磁体模型的基本原理，其中即使相对论能带分裂变得相当大，SSG 对线性二色性的预测仍然非常准确。 我们通过对两种互变磁性候选物的第一性原理计算，进一步确定了该框架的预测能力：锕系元素 UCr2Si2C，尽管其自旋轨道耦合很强，并且磁对称性具有明显的各向异性，但其光学吸收几乎保持各向同性；过渡金属氟化物 RbMnF4，其中双折射通过仅由 SSG 出现的对称性限制在单个平面内。 最后，我们将这一概念扩展到共面非共线反铁磁体 ScMnO3 的自旋霍尔响应，其中 SSG 解释了计算的自旋霍尔系数的层次结构，并证明了它们与自旋电子学的直接相关性。
**讨论重点：** 在这里，我们系统地展示了在非相对论水平上运行的自旋空间群（SSG）为分析磁体的各种光学响应提供了更广泛和更具预测性的框架。然而，大多数光学可观测量主要受非相对论物理学控制，因此纯粹基于 MSG 的描述可能会忽略重要的见解。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Zero-point theorems in quantum many-body physics

- Source: arXiv
- Date: 2026-08-16T05:29:13Z
- Venue: cond-mat.str-el, cond-mat.stat-mech, hep-th
- Authors: Yuan Yao
- Link: https://arxiv.org/abs/2608.15542v1
- Score: 16.0
- Match: 标题匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 我们基于不同维度的量子自旋系统相图中光谱间隙不可避免的零点，提出了几种零点类型论证。我们考虑扩展仅包含一个参数的传统零点定理的哈密顿量多参数族。与零点定理类似，我们只沿着参数边界施加与模型无关的变换关系，而不是指定任何低能动力学或响应。我们进一步给出一系列猜想，以统一的方式概括我们的陈述。 我们的结果对任意高维量子自旋模型中的关键现象的可能相关算子给出了强大且通用的独立于模型的约束。
**讨论重点：** 我们基于不同维度的量子自旋系统相图中光谱间隙不可避免的零点，提出了几种零点类型论证。与零点定理类似，我们只沿着参数边界施加与模型无关的变换关系，而不是指定任何低能动力学或响应。 结合关键词看，阅读时应重点关注量子多体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 10. Rapid supercurrent decay in Mn$_5$Si$_3$ Josephson junctions

- Source: arXiv
- Date: 2026-08-14T19:35:33Z
- Venue: cond-mat.supr-con, cond-mat.mes-hall
- Authors: Arjun Sapkota, Kurt Lorenzen, Tyler Kuhn, Juan Gomez, Demet Korucu, Robert M. Klaes
- Link: https://arxiv.org/abs/2608.14842v1
- Score: 16.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 近两周发布

**中文摘要：** 理论工作预测，包含金属交变磁势垒的约瑟夫森结应显示临界电流的 $0$-$π$ 转变，作为势垒厚度和温度的函数，超电流的衰减和振荡周期取决于晶轴相对于传输方向的方向。 受这些预测的启发，以及外延 Mn$_5$Si$_3$ 薄膜中交变磁性引起的补偿磁相位的报告，我们制造并测量了改变 Mn$_5$Si$_3$ 势垒厚度的 Nb/Pt/Mn$_5$Si$_3$/Pt/Nb 约瑟夫森结。临界电流以单指数形式衰减超过四个数量级，衰减长度为 $ xi_{\text{Mn}_5\text{Si}_3} = 0.31 \pm 0.03$ nm，比报道的包含金属反铁磁体 FeMn、Cr ​​和 NiMn 的约瑟夫森结要短。 Mn$_5$Si$_3$ 势垒的垂直于平面的电流电阻率估计为 $320 \pm 10 μΩ\,$cm。在采样的势垒厚度处没有解析出 $0$-$π$ 转变，并且具有 1 nm 势垒的结的临界电流的温度依赖性是平滑且单调的。 我们讨论了势垒微观结构、其不确定的磁相以及快速衰变造成的狭窄厚度窗口方面缺乏可解析的转变，并确定具有明确晶体取向的势垒作为未来交磁约瑟夫森物理测试的关键要求。
**讨论重点：** 受这些预测的启发，以及外延 Mn$_5$Si$_3$ 薄膜中交变磁性引起的补偿磁相位的报告，我们制造并测量了改变 Mn$_5$Si$_3$ 势垒厚度的 Nb/Pt/Mn$_5$Si$_3$/Pt/Nb 约瑟夫森结。临界电流以单指数形式衰减超过四个数量级，衰减长度为 $ xi_{\text{Mn}_5\text{Si}_3} = 0.31 \pm 0.03$ nm，比报道的包含金属反铁磁体 FeMn、Cr ​​和 NiMn 的约瑟夫森结要短。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。
