# Latest papers for 程旭丽

Updated: 2026-08-21T01:02:22.357954+00:00
Window: last 14 days

## Notes

- arXiv query failed for 凝聚态物理强关联体系和多铁性质: HTTP Error 429: Unknown Error
- 凝聚态物理强关联体系和多铁性质 returned 1 papers; target range is 5-10.

## 机器学习分子动力学模拟与热力学性质

### 1. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 15.0
- Match: 标题匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 然而，多组件批量 MD 模拟仍然难以实现，因为现有 MLIP 的 HBM 足迹（对于单组件系统来说已经很大）在多组件场景中呈爆炸性增长。本文提出了一种 HBM 占用空间较小的 MLIP（不到现有 MLIP 的 3%），仅使用数百个 GPU 即可解锁多组件批量 MD。这是通过首先将特征向量和中间张量识别为现有 MLIP 中 HBM 足迹的两个主要贡献者来实现的。 为了解决这两个来源，通过引入物理和化学知识来降低特征向量的维数，并通过积极地将所有内核融合到单个巨型内核中来消除中间张量。在评估中，所提出的MLIP使用了144个NVIDIA A100 GPU在具有1.14x10^9原子的6分量体系统上执行MD模拟，而此前这种MD模拟空间尺度仅限于一元系统，并且通常在配备数万个GPU的高端超级计算机上实现。
**讨论重点：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training

- Source: arXiv
- Date: 2026-08-17T11:15:35Z
- Venue: physics.chem-ph, physics.atom-ph
- Authors: Marie Bluntzer, Jules Tilly, Christoph Brunken
- Link: https://arxiv.org/abs/2608.16418v1
- Score: 11.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 训练集的质量和多样性是机器学习原子间势 (MLIP) 可靠性的关键决定因素，但完整使用大量数据集通常是不切实际且多余的，因此智能数据选择至关重要。然而，一个主要瓶颈是缺乏用于统一访问、整理和二次采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面差异很大。 我们使用 ChemReporter 解决了这一差距，这是一个与方法无关的模块化框架，可将任意分子和材料数据集转换为统一的、可查询的表示形式，并将结果直接导出到 MLIP 就绪的训练数据中。 ChemReporter 分三个解耦阶段运行：处理，将原始数据集解析为分区的 Apache Parquet 存储库，其中包含结构、物理和化学元数据；查询，通过 CLI 或 Python API 使用任意选择标准（从简单的物理约束到自定义的用户定义策略）过滤和采样此存储库；导出，将选定的子集流式传输到 HDF5 文件中，以便直接在现代 MLIP 训练框架中使用。 在整个过程中，每个导出的数据点都可以追溯到其原始源条目，并且在相同的配置和查询数据库版本的情况下，可以可靠地再现数据集导出。由于数据以可查询、磁盘支持的格式存储，ChemReporter 可以处理远远大于可用内存的数据集，从而使其能够在标准计算基础设施上扩展到数十亿结构的数据集。 ChemReporter 可在 GitHub 和 PyPI 上使用 Apache License 2.0。
**讨论重点：** 我们使用 ChemReporter 解决了这一差距，这是一个与方法无关的模块化框架，可将任意分子和材料数据集转换为统一的、可查询的表示形式，并将结果直接导出到 MLIP 就绪的训练数据中。然而，一个主要瓶颈是缺乏用于统一访问、整理和二次采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面差异很大。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Electrostatic Phenomenology Benchmarks for Machine-Learned Interatomic Potentials in Electrochemistry: Beyond the Energy-Force Metric

- Source: arXiv
- Date: 2026-08-14T10:03:18Z
- Venue: cond-mat.mtrl-sci, physics.chem-ph, physics.comp-ph
- Authors: Barbara Sumić, Ria Vasdev, Sudheesh Kumar Ethirajan, Jing Yang, Clotilde S. Cucinotta, Richard G. Hennig
- Link: https://arxiv.org/abs/2608.14153v1
- Score: 8.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 准确处理机器学习原子间势 (MLIP) 中的长程相互作用对于电化学模拟至关重要。然而，仅靠总能量和力误差不足以确定 MLIP 的物理精度，因为它们无法检测模型中的定性不一致，例如图像电荷吸引、介电屏蔽或电荷转移的预测。我们引入了一个基准套件 EPhEct（电化学静电现象），其中包含专门的测试用例，旨在评估电化学相关物理现象的 MLIP。 该测试探测金属电极处的图像电荷吸引力、作为离子和电子屏蔽探针的纵向和横向光学声子之间的分裂、界面水的偶极矩以及离子放电期间的费米能级钉扎。这些测试建立了一个定性诊断程序，作为总体能量指标的补充。
**讨论重点：** 我们引入了一个基准套件 EPhEct（电化学静电现象），其中包含专门的测试用例，旨在评估电化学相关物理现象的 MLIP。然而，仅靠总能量和力误差不足以确定 MLIP 的物理精度，因为它们无法检测模型中的定性不一致，例如图像电荷吸引、介电屏蔽或电荷转移的预测。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 6. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 铁（Fe）氧化的准确原子建模需要可靠的原子间势，这需要广泛且具有代表性的第一性原理数据集来训练原子间势。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。 我们提出了一种系统方法，基于原子团簇扩展 (ACE) 框架，为 Fe-O 系统开发首个可转移机器学习原子间势 (MLIP)。我们通过体积、表面和界面特性彻底验证了 ACE MLIP 在纯 Fe 和 Fe-O 系统中的准确性和功能。我们展示了使用 ACE MLIP 大规模 Fe 氧化模拟中 FeO 类结构的形成。 这项工作表明，PASS 方法产生了准确且可转移的 MLIP，它能够捕获氧化物生长的反应复杂性，同时保持扩展系统的计算实用性。
**讨论重点：** 在这项工作中，我们提出了微扰增强空间群结构采样（PASS）方法来生成由少于 10 个原子的小细胞结构组成的广泛且具有代表性的数据集。然而，铁氧（O）系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 7. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

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
- Link: https://arxiv.org/abs/2607.18099v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 耐火高熵合金是高温应用的有希望的候选者，但成分对其化学排序途径和机械性能的影响仍不清楚。在这里，采用通用 MLIP 与 MC 和 MD 模拟相结合来研究 (MoCrTi)(100-x)Alx 合金的温度依赖性热力学和机械行为。 原子构型、亚晶格占据和模拟衍射强度揭示了低温下明显的 B2 型化学有序性，其中 Mo 和 Al 占据一个亚晶格，Cr 和 Ti 占据另一个亚晶格。配置热容和SRO参数进一步揭示了有序路径的强烈组成依赖性。 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出单一的主导有序阶段，涉及多个 B2 型对相关性的协同变化。相比之下，Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 表现出两个不同的有序阶段。 它们的低温特征主要分别与Mo-Al和Al-Al相关性的变化相关，而它们的高温特征则涉及其余B2型对相关性的集体变化。化学排序也从根本上改变了机械刚度的成分依赖性。无序构型的弹性常数随着 Al 含量的降低而近似单调增加，而有序构型的弹性常数表现出非单调依赖性，并在 Mo30Cr30Ti30Al10 中达到最大值。 这种异常增强源于 SRO 引起的原子对（尤其是 Mo-Cr 对）的重新分布。这些结果在合金成分、多级化学排序和机械刚度之间建立了直接的原子联系，为通过成分控制调整 RHEA 的机械行为提供了指导。
**讨论重点：** 在这里，采用通用 MLIP 与 MC 和 MD 模拟相结合来研究 (MoCrTi)(100-x)Alx 合金的温度依赖性热力学和机械行为。原子构型、亚晶格占据和模拟衍射强度揭示了低温下明显的 B2 型化学有序性，其中 Mo 和 Al 占据一个亚晶格，Cr 和 Ti 占据另一个亚晶格。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

## 凝聚态物理强关联体系和多铁性质

### 1. Efficient quantum implementation of dynamical mean field theory for correlated materials

- Source: Journal
- Date: 2026-08-17
- Venue: npj Computational Materials
- Authors: Norman Hogan, Efekan Kökcü, Thomas Steckmann, Liam P. Doak, Carlos Mejuto-Zaera, Daan Camps
- Link: https://doi.org/10.1038/s41524-026-02289-2
- Score: 13.0
- Match: 标题匹配 dynamical mean field theory; 近两周发布

**中文摘要：** 当前元数据未提供原文摘要。论文题目为“Efficient quantum implementation of dynamical mean field theory for correlated materials”。
**讨论重点：** 结合关键词看，阅读时应重点关注动力学平均场理论相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。
