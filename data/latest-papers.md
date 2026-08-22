# Latest papers for 程旭丽

Updated: 2026-08-22T00:58:54.353792+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 14.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 然而，多组件批量 MD 模拟仍然难以实现，因为现有 MLIP 的 HBM 足迹（对于单组件系统来说已经很大）在多组件场景中呈爆炸性增长。本文提出了一种 HBM 占用空间较小的 MLIP（不到现有 MLIP 的 3%），仅使用数百个 GPU 即可解锁多组件批量 MD。这是通过首先将特征向量和中间张量识别为现有 MLIP 中 HBM 足迹的两个主要贡献者来实现的。 为了解决这两个来源，通过引入物理和化学知识来降低特征向量的维数，并通过积极地将所有内核融合到单个巨型内核中来消除中间张量。在评估中，所提出的MLIP使用了144个NVIDIA A100 GPU在具有1.14x10^9原子的6分量体系统上执行MD模拟，而此前这种MD模拟空间尺度仅限于一元系统，并且通常在配备数万个GPU的高端超级计算机上实现。
**讨论重点：** 与纳米材料相反，块体材料需要在大空间尺度（~10^9 个原子或更多）上进行分子动力学 (MD) 模拟，以充分捕获其原子尺度的物理特性。此前，机器学习原子间势（MLIP）的引入已将MD扩展到如此规模，但即使是单组件批量系统也需要在高端超级计算机上使用数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training

- Source: arXiv
- Date: 2026-08-17T11:15:35Z
- Venue: physics.chem-ph, physics.atom-ph
- Authors: Marie Bluntzer, Jules Tilly, Christoph Brunken
- Link: https://arxiv.org/abs/2608.16418v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 训练集的质量和多样性是机器学习原子间势 (MLIP) 可靠性的关键决定因素，但完整使用大量数据集通常是不切实际且多余的，因此智能数据选择至关重要。然而，一个主要瓶颈是缺乏用于统一访问、整理和二次采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面差异很大。 我们使用 ChemReporter 解决了这一差距，这是一个与方法无关的模块化框架，可将任意分子和材料数据集转换为统一的、可查询的表示形式，并将结果直接导出到 MLIP 就绪的训练数据中。 ChemReporter 分三个解耦阶段运行：处理，将原始数据集解析为分区的 Apache Parquet 存储库，其中包含结构、物理和化学元数据；查询，通过 CLI 或 Python API 使用任意选择标准（从简单的物理约束到自定义的用户定义策略）过滤和采样此存储库；导出，将选定的子集流式传输到 HDF5 文件中，以便直接在现代 MLIP 训练框架中使用。 在整个过程中，每个导出的数据点都可以追溯到其原始源条目，并且在相同的配置和查询数据库版本的情况下，可以可靠地再现数据集导出。由于数据以可查询、磁盘支持的格式存储，ChemReporter 可以处理远远大于可用内存的数据集，从而使其能够在标准计算基础设施上扩展到数十亿结构的数据集。 ChemReporter 可在 GitHub 和 PyPI 上使用 Apache License 2.0。
**讨论重点：** 我们使用 ChemReporter 解决了这一差距，这是一个与方法无关的模块化框架，可将任意分子和材料数据集转换为统一的、可查询的表示形式，并将结果直接导出到 MLIP 就绪的训练数据中。然而，一个主要瓶颈是缺乏用于统一访问、整理和二次采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面差异很大。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 基础机器学习原子间势（MLIP）能够以比第一原理方法低得多的计算成本进行原子模拟，但它们在结构几何形状上的可靠性仍然没有得到充分的了解。在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。 我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。在没有任何训练的情况下，仅在参考能量对准后，最佳零射击模型（ORB-V3）的能量和力均方根误差分别达到 6 meV/atom 和 197.3 meV/Å，其中颈部和线配置中的力误差最大。然后，我们比较零样本推理、微调和从头开始训练策略。与从头开始训练相比，微调产生的能量和力量误差更低，而两者都需要相当的挂钟时间。 特定于几何形状的微调提高了域内精度，但经常产生向其他结构类别的负转移，而混合几何微调则减少了跨几何误差。对弹性和振动特性、表面能和颈部动力学的评估进一步表明，基于平均能量和力误差的排名并不能普遍预测属性水平的行为。这些结果表明，在将基础 MLIP 应用于低配位（离子）纳米结构时，几何形状多样的目标数据和独立的物理验证是必要的。
**讨论重点：** 在这里，我们构建了一个 ZrO2 配置的密度泛函理论数据集，涵盖块状、板状、颗粒、颈部和原子细线环境，其动机是通过实验观察到的 ZrO2 脱烧结过程（涉及颈部细化和原子线形成）。我们首先对 26 个预训练的 MLIP 进行基准测试，并观察零样本预测中明显的几何相关退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。使用 DNNP 可以对具有数千个原子的大型 $α$-SiO$_2$ 单元进行接近 DFT 精度的原子建模。 特别是，DNNP 使我们能够获得由电子温度突然升高激发的 $α$-SiO$_2$ 的精确声子能带结构和分子动力学 (MD)。随着电子温度 $T_e$ 的增加，发现 $α$-SiO$_2$ 出现明显的晶格失稳，表现为违反弹性稳定性标准、体积大幅膨胀、体积模量急剧下降以及由于反键态占据而导致 Si-O 键逐渐减弱。 根据电子和声子能带结构，我们估计了 Frohlich 耦合常数，该常数随着 $T_e$ 的增加而减小，表明在电子温度升高时会交叉到 $α$-SiO$_2$ 的非极性相。 Bader 电荷分析证实了这一点。我们还建议在 $T_e > 2$ eV 时应强烈抑制极性光学声子散射。从大单元 DNNP-MD 模拟中，我们表明，在最初的几百飞秒内，并未实现由麦克斯韦-玻尔兹曼分布定义的明确热平衡。 这种行为解释了 $T_e$ 突然上升后动力学温度的非单调平衡。当 $T_e$ 升至 2.6 eV 后，Si 和 O 原子首先在两个不同的温度下分别达到平衡，表明存在原子流体相，这与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度机器学习第一原理方法来研究电子激发 $α$-SiO$_2$ 中的超快晶格动力学。基于电子温度依赖性密度泛函理论 (DFT) 的从头算分子动力学 (AIMD) 用于训练电子温度依赖性深度神经网络势 (DNNP)。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 5. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

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

**中文摘要：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 HDNNP 准确地描述了 B19$^\prime$ 和 B33 相的相对稳定性，包括 meV/原子数量级的细微能量差异。预测的堆垛层错能量景观具有强烈的各向异性，揭示了优先剪切路径，为变形和孪晶机制提供了原子学的见解。有限温度分子动力学模拟进一步能够研究作为温度函数的无约束结构演化。 总体而言，开发的 HDNNP 为纳秒时间尺度上包含数十万个原子的马氏体 NiTi 系统的复杂结构和功能行为的原子模拟提供了坚实的基础。
**讨论重点：** 我们提出了一种针对 NiTi 形状记忆合金马氏体相的高维神经网络势 (HDNNP)，并根据密度泛函理论 (DFT) 数据进行了训练。这项工作的一个核心方面是对控制结构演化的关键特性（包括平衡晶体结构、弹性常数、广义堆垛层错能和振动谱）的基础 DFT 参考方法的潜力进行系统验证。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 9. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 耐火高熵合金是高温应用的有希望的候选者，但成分对其化学排序途径和机械性能的影响仍不清楚。在这里，采用通用 MLIP 与 MC 和 MD 模拟相结合来研究 (MoCrTi)(100-x)Alx 合金的温度依赖性热力学和机械行为。 原子构型、亚晶格占据和模拟衍射强度揭示了低温下明显的 B2 型化学有序性，其中 Mo 和 Al 占据一个亚晶格，Cr 和 Ti 占据另一个亚晶格。配置热容和SRO参数进一步揭示了有序路径的强烈组成依赖性。 Mo25Cr25Ti25Al25 和 Mo32Cr32Ti32Al4 合金表现出单一的主导有序阶段，涉及多个 B2 型对相关性的协同变化。相比之下，Mo28Cr28Ti28Al16 和 Mo30Cr30Ti30Al10 表现出两个不同的有序阶段。 它们的低温特征主要分别与Mo-Al和Al-Al相关性的变化相关，而它们的高温特征则涉及其余B2型对相关性的集体变化。化学排序也从根本上改变了机械刚度的成分依赖性。无序构型的弹性常数随着 Al 含量的降低而近似单调增加，而有序构型的弹性常数表现出非单调依赖性，并在 Mo30Cr30Ti30Al10 中达到最大值。 这种异常增强源于 SRO 引起的原子对（尤其是 Mo-Cr 对）的重新分布。这些结果在合金成分、多级化学排序和机械刚度之间建立了直接的原子联系，为通过成分控制调整 RHEA 的机械行为提供了指导。
**讨论重点：** 在这里，采用通用 MLIP 与 MC 和 MD 模拟相结合来研究 (MoCrTi)(100-x)Alx 合金的温度依赖性热力学和机械行为。原子构型、亚晶格占据和模拟衍射强度揭示了低温下明显的 B2 型化学有序性，其中 Mo 和 Al 占据一个亚晶格，Cr 和 Ti 占据另一个亚晶格。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

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

### 1. Mirror Chern insulators in two-dimensional altermagnetic Tc$_2$Cl$_2$O and Tc$_2$Br$_2$O

- Source: arXiv
- Date: 2026-08-20T07:23:14Z
- Venue: cond-mat.mtrl-sci
- Authors: Rong Wang, Ruo-Yu Ning, Zhi-Hua Yan, Si Li
- Link: https://arxiv.org/abs/2608.19725v1
- Score: 30.0
- Match: 摘要匹配 altermagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials

**中文摘要：** 交变磁性和晶带拓扑之间的相互作用为实现具有独特的自旋相关特性的非常规拓扑相提供了一条有趣的途径。在这里，基于第一性原理计算和理论分析，我们将单层 $\mathrm{Tc}_2X_2\mathrm{O}$ ($X$ = Cl, Br) 识别为二维互磁镜陈绝缘体族。在没有自旋轨道耦合（SOC）的情况下，两个单层都表现出具有镜像自旋耦合的鲁棒交变磁性，并且在费米能级附近的每个自旋通道中拥有两个对称保护的韦尔点。 相反自旋通道中的 Weyl 点具有不同的镜像对称特征值 $m_z=\pm i$。包含 SOC 后，Weyl 点出现间隙，两个镜像扇区获得相反的陈数 ${\cal {C}}_{+}=1$ 和 ${\cal {C}}_{-}=-1$，从而产生非零镜像陈数 ${\cal {C}}_m=1$。低能量 $k\cdot p$ 模型捕获 Weyl 点的对称性保护，并阐明其 SOC 引起的质量间隙和拓扑特征。 此外，所得的镜陈绝缘相在体带隙内具有螺旋边缘态，并表现出量子化的自旋霍尔电导率。我们的工作在交变磁学和镜像陈拓扑之间建立了直接联系，并为探索二维交变磁材料中的非常规拓扑和自旋相关现象提供了一个有前途的平台。
**讨论重点：** 低能量 $k\cdot p$ 模型捕获 Weyl 点的对称性保护，并阐明其 SOC 引起的质量间隙和拓扑特征。在这里，基于第一性原理计算和理论分析，我们将单层 $\mathrm{Tc}_2X_2\mathrm{O}$ ($X$ = Cl, Br) 识别为二维互磁镜陈绝缘体族。 结合关键词看，阅读时应重点关注交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Altermagnetic memcapacitors

- Source: arXiv
- Date: 2026-08-19T22:23:01Z
- Venue: cond-mat.mes-hall
- Authors: Martin Latorre, Alvaro S. Nunez
- Link: https://arxiv.org/abs/2608.19476v1
- Score: 29.0
- Match: 摘要匹配 multiferroic; 摘要匹配 multiferroic materials; 标题匹配 altermagnetic; 标题匹配 altermagnet

**中文摘要：** 我们提出了基于交变多铁材料的自旋电子磁电容效应。我们将稀土钒酸盐 RVO$_3$ 确定为一个具体平台，所有关键参数都与测量的属性相关。 在振荡电场下，产生的电荷和自旋电流会追踪在零场切向闭合的收缩磁滞回线（这是记忆电容、2 型记忆器件行为的标志），充电电流密度超过了优化自旋转移扭矩磁隧道结所报道的最低确定性开关电流密度的约 3.6 倍。 我们本着自旋相关的 Rice-Mele 模型的精神，通过 Su-Schrieffer-Heeger 型键调制，从理论上将该系统建模为二聚双轨道 $d$ 波交变磁晶格，从而将交变磁序与场可切换电荷和自旋极化耦合起来。相关的极化环在零场处切向闭合，并产生符号变化、历史相关的“蝴蝶”差分电容，从而将该设备识别为真正的记忆电容器。 两种响应都受到相同的反演对称性的保护，因此电荷和自旋通道同时切换，无需单独控制。这些结果建立了交磁多铁性材料，在 RVO$_3$ 中具体实现，作为组合电和自旋电子存储器的高效、非易失性平台。
**讨论重点：** 我们提出了基于交变多铁材料的自旋电子磁电容效应。我们本着自旋相关的 Rice-Mele 模型的精神，通过 Su-Schrieffer-Heeger 型键调制，从理论上将该系统建模为二聚双轨道 $d$ 波交变磁晶格，从而将交变磁序与场可切换电荷和自旋极化耦合起来。 结合关键词看，阅读时应重点关注多铁性、多铁材料、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Valley- and Spin-Dependent Electronic and Transport Properties of Two-Dimensional Altermagnetic Titanium-Based Chalcogenide Halides

- Source: arXiv
- Date: 2026-08-20T07:34:49Z
- Venue: cond-mat.mtrl-sci
- Authors: Ruo-Yu Ning, Zhi-Hua Yan, Jin-Yang Li, Yong-Kun Wang, Si Li
- Link: https://arxiv.org/abs/2608.19734v1
- Score: 27.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 摘要匹配 altermagnetic materials; 最近 3 天发布

**中文摘要：** 交变磁体 (AM) 将完全补偿的磁化强度与动量相关的自旋分裂相结合，但表现出特殊谷特性的本征交变磁材料仍然很少。在这里，我们将单层钛基硫族化物卤化物 Ti$_2X_2Y$ ($X$ = F, Cl, Br, I; $Y$ = O, S, Se, Te) 确定为二维互磁谷材料的新家族。这些单层表现出强大的 $d$ 波交变磁序、半导体带隙和明显的自旋极化谷特性。 我们表明，单轴应变打破了谷简并性，引发了巨大的谷极化以及可调谐的压磁响应。面内电场产生非共线自旋电流，而自旋轨道耦合则产生反常霍尔效应、谷选择性线性二向色性和磁光克尔效应。这些发现将 Ti$_2X_2Y$ 单层确立为一个多功能平台，用于探索二维交替磁体中自旋和谷相关的电子、光学和输运现象。
**讨论重点：** 交变磁体 (AM) 将完全补偿的磁化强度与动量相关的自旋分裂相结合，但表现出特殊谷特性的本征交变磁材料仍然很少。在这里，我们将单层钛基硫族化物卤化物 Ti$_2X_2Y$ ($X$ = F, Cl, Br, I; $Y$ = O, S, Se, Te) 确定为二维互磁谷材料的新家族。 结合关键词看，阅读时应重点关注交变磁性、交变磁性材料相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Structural complexity of an SU(3) Fermi Hubbard model

- Source: arXiv
- Date: 2026-08-20T14:58:26Z
- Venue: cond-mat.quant-gas, cond-mat.str-el
- Authors: Jiani Fu, Zewen Zhang, Eduardo Ibarra-García-Padilla
- Link: https://arxiv.org/abs/2608.20131v1
- Score: 20.0
- Match: 标题匹配 Hubbard model; 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 二维量子气体显微镜为使用超冷原子研究量子多体系统提供了无与伦比的工具。对于 SU(2) 费米哈伯德模型 (FHM)，获得自旋分辨投影测量对于量化相关函数和绘制相图至关重要。 SU(N) FHM 很好地描述了超冷碱土原子实验的量子气体显微镜，并预测其具有奇特的基态相，这需要开发无理论的数值技术来从投影测量中提取物理信息。为此，我们评估了 1/3$ 填充的方格子中 SU(3) FHM 快照的多尺度结构复杂性。 我们采用平均场理论来生成自旋分辨密度分布，并使用矩形粗粒度窗口计算其结构复杂性。我们证明这些复杂性与相关的物理可观测值（例如纠缠熵）相关，并且对于定位相边界极其敏感。这里提出的结果验证了结构复杂性作为分析 SU(N) 量子气体显微镜输出的高效可靠的工具，提供了无需理论的特性，可以立即进行实验。
**讨论重点：** 二维量子气体显微镜为使用超冷原子研究量子多体系统提供了无与伦比的工具。对于 SU(2) 费米哈伯德模型 (FHM)，获得自旋分辨投影测量对于量化相关函数和绘制相图至关重要。 结合关键词看，阅读时应重点关注Hubbard 模型、量子多体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. A low-temperature setup for lock-in technique based dynamic magnetoelectric coupling measurements

- Source: arXiv
- Date: 2026-08-20T12:24:40Z
- Venue: cond-mat.mtrl-sci
- Authors: Balwant Singh Chauhan, Priyanka Sharma, Rie Y. Umetsu, Ratnamala Chatterjee
- Link: https://arxiv.org/abs/2608.19956v1
- Score: 20.0
- Match: 摘要匹配 multiferroic; 标题匹配 magnetoelectric coupling; 最近 3 天发布

**中文摘要：** 二维范德华 (vdW) 磁体和单分子磁体 (SMM) 等新兴材料类别中的磁电 (ME) 现象为下一代低温存储器和量子技术带来了巨大前景。然而，这些系统中的 ME 耦合主要出现在低温下，因此敏感的、低温兼容的 ME 表征技术至关重要。 为了满足这一要求，我们报告了基于定制闭环制冷机的设置的设计、验证和性能，该设置用于在高达 7.5 kOe 的直流磁场下在 20-300 K 范围内进行动态锁定 ME 耦合测量。还提出了减轻寄生感应背景信号的关键设计考虑因素。该装置在 CoFe2O4-BaTiO3 (CFO-BTO) 颗粒复合材料上进行了验证，再现了典型的室温蝶形 ME 环路，在 ~ 3 kOe 时最大 ME 系数值为 0.23 mV/cm-Oe。 与温度相关的测量解决了约 200 K 和 280 K 的 ME 异常，与 BaTiO3 的菱形-斜方晶系和斜方晶-四方结构转变相一致，并且通过在没有低温恒温器重新配置的情况下对同一样品进行同步介电测量来证实。该仪器能够在低至 20 K 的温度下进行可靠的 ME 和介电表征，非常适合探测多铁复合材料和量子材料中的弱磁电耦合和相变。
**讨论重点：** 为了满足这一要求，我们报告了基于定制闭环制冷机的设置的设计、验证和性能，该设置用于在高达 7.5 kOe 的直流磁场下在 20-300 K 范围内进行动态锁定 ME 耦合测量。然而，这些系统中的 ME 耦合主要出现在低温下，因此敏感的、低温兼容的 ME 表征技术至关重要。 结合关键词看，阅读时应重点关注多铁性、磁电耦合相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 6. Nonlinear Drude weight of the one-dimensional Hubbard model

- Source: arXiv
- Date: 2026-08-20T17:07:16Z
- Venue: cond-mat.str-el, cond-mat.quant-gas, cond-mat.stat-mech
- Authors: Tetsuya Iwasaki, Hosho Katsura
- Link: https://arxiv.org/abs/2608.20269v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 我们通过将精确的 Bethe-ansatz 计算与低能有效场理论相结合，研究一维排斥 Hubbard 模型中的非线性 Drude 权重 (NLDW)。在季度填充时，我们首先推导出 NLDW 的强耦合展开式，并在广泛的相互作用强度范围内以数值方式对其进行确认。然后，我们将数值结果与 Tomonaga-Luttinger 液体 (TLL) 描述（包括不相关扰动）的预测进行比较。 虽然能带曲率校正对高阶 NLDW 产生有限的贡献，但当 Drude 权重的阶 $n$ 超过由 TLL 参数确定的阈值时，Umklapp 交互会预测发散的 NLDW。相比之下，精确的 Bethe-ansatz 结果的有限尺寸缩放表明，所有计算的 NLDW 在热力学极限下仍然是有限的，揭示了精确结果与低能有效场理论的预测之间的差异。在半填充时，我们分析了 Mott 金属-绝缘体转变过程中 NLDW 的有限尺寸缩放。 我们推导了它们在绝缘阶段的渐近行为，并提出了 NLDW 在临界点附近的超尺度模拟，并得到了数值验证。我们的结果阐明了一维哈伯德模型中非线性输运系数的相互作用依赖性和临界标度，并强调了传统低能有效描述高阶输运的局限性。
**讨论重点：** 我们推导了它们在绝缘阶段的渐近行为，并提出了 NLDW 在临界点附近的超尺度模拟，并得到了数值验证。我们通过将精确的 Bethe-ansatz 计算与低能有效场理论相结合，研究一维排斥 Hubbard 模型中的非线性 Drude 权重 (NLDW)。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Equations of Tree Tensor Network Varieties

- Source: arXiv
- Date: 2026-08-19T16:12:21Z
- Venue: math.AG, cond-mat.str-el, math.AC
- Authors: Serkan Hoşten, Niharika Chakrabarty Paul, Otto T. P. Schmidt, Dmitry Skurt
- Link: https://arxiv.org/abs/2608.19071v1
- Score: 16.0
- Match: 标题匹配 tensor network; 最近 3 天发布

**中文摘要：** 我们证明，树张量网络变体，包括张量训练变体，是与间隔树相关的一般马尔可夫模型。这使我们能够证明这些品种的主要理想是由矩阵扁平化的次要产物产生的。在张量序列变体的情况下，我们讨论这些次要是否形成 Gröbner 基，并提供一种组合方法来计算 $3$ 阶张量序列的度。
**讨论重点：** 在张量序列变体的情况下，我们讨论这些次要是否形成 Gröbner 基，并提供一种组合方法来计算 $3$ 阶张量序列的度。这使我们能够证明这些品种的主要理想是由矩阵扁平化的次要产物产生的。 结合关键词看，阅读时应重点关注张量网络相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。

### 8. Anti-spin Laue groups: classification of anti-altermagnets and their representative minimal models

- Source: arXiv
- Date: 2026-08-19T15:54:23Z
- Venue: cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Colin Lange, Rodrigo Jaeschke-Ubiergo, Alexander Mook, Jairo Sinova
- Link: https://arxiv.org/abs/2608.19056v1
- Score: 16.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 反交变磁体表现出奇宇称非相对论性自旋分裂，但与偶宇称交变磁体不同，它们的动量空间对称性缺乏类似于自旋劳厄群的简化分类。在这里，我们引入了反自旋劳厄群，将其分为三个不同的类别，并确定了描述该非常规类别的奇宇称部分波特征的 21 个群。它们与 10 个自旋劳厄群互变磁体一起，完成了具有共线动量空间自旋极化的非相对论非常规磁体的分类。 反自旋劳厄群还通过仅保留其对共线动量空间自旋极化的作用来提供自旋空间（点）群的多对一减少，从而直接编码对称性强制的节点自旋分裂特征。在此基础上，我们开发了一种系统模型构建算法，可生成最小的、面向材料的四频带模型。该框架将奇宇称和偶宇称非常规磁体置于统一的动量空间对称性描述中同等的地位。
**讨论重点：** 在这里，我们引入了反自旋劳厄群，将其分为三个不同的类别，并确定了描述该非常规类别的奇宇称部分波特征的 21 个群。在此基础上，我们开发了一种系统模型构建算法，可生成最小的、面向材料的四频带模型。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Hubb_DMFT and Wan2mb_DMFT: Continuous-Time Quantum Monte Carlo Solvers for Single- and Multi-Orbital Hubbard Model

- Source: arXiv
- Date: 2026-08-19T04:50:36Z
- Venue: cond-mat.str-el
- Authors: A. A. Katanin
- Link: https://arxiv.org/abs/2608.18540v1
- Score: 16.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 我们提出了两个相关的定制软件包 Hubb_DMFT 和 Wan2mb_DMFT，旨在求解强相关电子系统的动态平均场理论 (DMFT) 方程。 Hubb_DMFT 针对单带 Hubbard 模型进行了调整，提供了一种快速计算局部自能以及双粒子费米子和三角形费米子-玻色子电荷和自旋顶点的方法，而 Wan2mb_DMFT 将此功能扩展到现实的多轨道系统，直接将 Wannier 紧束缚哈密顿量与多体求解器连接起来。 两种代码均基于 iQIST v.0.7 杂质求解器，并利用经过修改和内部集成的连续时间量子蒙特卡罗 (CT-QMC) 核心以及混合扩展 (CT-HYB) 框架和改进的自能和顶点估计器，用于密度-密度相互作用，确保量子杂质问题的数值精确解决方案。
**讨论重点：** 我们提出了两个相关的定制软件包 Hubb_DMFT 和 Wan2mb_DMFT，旨在求解强相关电子系统的动态平均场理论 (DMFT) 方程。 Hubb_DMFT 针对单带 Hubbard 模型进行了调整，提供了一种快速计算局部自能以及双粒子费米子和三角形费米子-玻色子电荷和自旋顶点的方法，而 Wan2mb_DMFT 将此功能扩展到现实的多轨道系统，直接将 Wannier 紧束缚哈密顿量与多体求解器连接起来。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. High-field fate of the Kitaev quantum spin liquid in $α$-RuCl$_3$

- Source: arXiv
- Date: 2026-08-19T04:26:09Z
- Venue: cond-mat.str-el
- Authors: K. Imamura, R. Ohno, Y. C. Tsuzuki, Y. Akui, R. Namba, K. Ishihara
- Link: https://arxiv.org/abs/2608.18530v1
- Score: 16.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** Kitaev 量子自旋液体 (KQSL) 具有由流动的马约拉纳准粒子和间隙 $Z_2$ 通量（视觉）描述的分段激发，为新兴拓扑物质提供了一个平台。然而，这种状态是否能在强磁场下生存仍然是一个悬而未决的问题。 层状蜂窝磁体 $α$-RuCl$_3$ 是一种领先的候选材料：$\sim$ 7 T 的面内场抑制反铁磁有序并诱导量子无序相，该相表现出与马约拉纳激发一致的特征，包括反常热霍尔效应和场角依赖性比热。在更高的磁场下，磁化强度接近饱和，表明向自旋极化状态的转变，但这些极限之间的微观演化仍未解决。 在这里，我们报告了高达 24 T 的高场比热测量，揭示了 $μ_0H^*\approx$15 T 处的明显交叉，超过该交叉点，基塔耶夫的微扰描述就失效了。高于 $H^*$ 时，比热的特征六倍角调制崩溃，并且激发间隙偏离预测的 $H^3$ 比例。 同时，间隙随着磁场的增加而减小，并且面内磁化各向异性持续到 $\sim$ 24 T，两者都与微不足道的自旋极化状态形成鲜明对比，表明即使在 $\sim$ 磁化饱和度的 90% 时，KQSL 特征仍然保留。这些结果表明，$α$-RuCl$_3$ 中的 KQSL 远远超出了微扰窗口，在最终让位于自旋极化之前，以非微扰状态持续存在，其中马约拉纳和视觉能量尺度合并。
**讨论重点：** Kitaev 量子自旋液体 (KQSL) 具有由流动的马约拉纳准粒子和间隙 $Z_2$ 通量（视觉）描述的分段激发，为新兴拓扑物质提供了一个平台。然而，这种状态是否能在强磁场下生存仍然是一个悬而未决的问题。 结合关键词看，阅读时应重点关注量子自旋液体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。
