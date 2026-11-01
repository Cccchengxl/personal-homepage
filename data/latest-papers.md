# Latest papers for 程旭丽

Updated: 2026-11-01T03:58:55.963121+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: HTTP Error 429: Unknown Error
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.

## 机器学习分子动力学模拟与热力学性质

### 1. Nitrogen vacancy cluster-mediated ferroelectric domain growth in wurtzite AlN

- Source: arXiv
- Date: 2026-10-22T10:56:32Z
- Venue: cond-mat.mtrl-sci
- Authors: Zijian Zhou, Kan-Hao Xue, Ziqi Pang, Heng Yu, Shanzhong Xie, Hang Liu
- Link: https://arxiv.org/abs/2610.31084v1
- Score: 12.0
- Match: 摘要匹配 deep potential molecular dynamics; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 我们进一步表明，钪掺杂促进$ V_\ mathrm {N} $的形成，从而增强缺陷介导的成核并减少$ E_\ mathrm {c} $。这些发现建立了管理薄膜畴生长动力学和宏观$ E_\ mathrm {c} $的多尺度机制，将实验观测与理想的晶体模拟相协调，并为低电压、可靠和可扩展的铁电器件提供缺陷工程原理。
**讨论重点：** 氮化铝基铁电体结合了高剩余极化、热稳定性、弱尺寸效应、宽带隙和后端工艺兼容性，使其有望实现高密度非易失性存储器。然而，它们的高矫顽场（ $ E_\ mathrm {c} $ ）和不清楚的极化切换机制限制了进一步的应用。 结合关键词看，阅读时应重点关注深度势分子动力学相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 2. Concentration-Dependent Speciation in ZnCl2 Electrolyte Solutions: Transferability of Machine-Learning Interatomic Potentials and Speciation Sensitivity of EXAFS

- Source: arXiv
- Date: 2026-10-21T22:46:57Z
- Venue: physics.chem-ph
- Authors: Junhan Chen, Luke D. Gibson, Nadia N. Intan, Darren M Driscoll, Mahalingam Balasubramanian, John L. Fulton
- Link: https://arxiv.org/abs/2610.30513v1
- Score: 11.0
- Match: 摘要匹配 DeepMD; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS DFT治疗强烈影响协调自由能和聚集；排除与Zn相关的D3校正并不能系统地改善EXAFS一致性。CMD显示出更大的光谱差异和不一致的协调趋势。MACE-MATPES-r2SCAN改进了CMD ，产生了与DPMD-SCAN相当的光谱，提供了更一致的一致性和更高的计算效率。 邻域分辨分析表明，距离无序和散射路径干扰可以为不同的协调集合产生相似的EXAFS特征，这突出了严格采样和集合平均光谱以区分与氯桥接锌种类的必要性。
**讨论重点：** 我们将Zn K边缘扩展X射线吸收精细结构（ EXAFS ）测量与长时间尺度分子动力学（ MD ）相结合，使用机器学习原子间电位研究从稀释到30 m的ZnCl2水溶液。我们训练基于revPBE的DeepMD模型，包括或排除含锌对的D3校正，并将其与DPMD-SCAN、经典MD （ CMD ）和MACE-MATPES-r2SCAN进行比较。 结合关键词看，阅读时应重点关注DeepMD相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Source: arXiv
- Date: 2026-10-16T15:44:07Z
- Venue: cond-mat.mtrl-sci, cs.LG
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia
- Link: https://arxiv.org/abs/2610.23643v1
- Score: 10.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 在这里，我们通过将远程静电力和天然有效电荷（ BEC ）分析性地分离成全局静电计算和已知潜在电荷的严格局部导数来克服这一局限性。该配方保留了等变MLIP的空间可分解性，同时允许在不同边界条件下对能量、力、应力和BEC进行分布式评估。 该框架在\ texttt {nvalchemi}平台上实现为DPA4C-LR ，在四个GPU上扩展到520万个原子，其计算成本大约是其短程骨干网的两倍。经过能量和力的训练， DPA4C-LR准确地推断出BEC ，并再现了水的场相关红外光谱。 我们进一步展示了它的能力，恢复了松弛体\ ce {Pb (Mg_{1/3} Nb_{2/3}) O3}的特征极化迟滞，这种迟滞在较小的模拟中被有限尺寸效应所掩盖；预测了非晶态\ ce {Li_{0.9} NbO_{0.9} Cl_{4.1}}中的室温场驱动离子电导率为$ 6.8\ pm 0.7 $ ~ mS/cm ；并用平板校正的静电学对硅/金刚石界面上的界面热传输进行建模。
**讨论重点：** 严格的局部模型实现了高效的空间并行化，但忽略了远程相互作用，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。该框架在\ texttt {nvalchemi}平台上实现为DPA4C-LR ，在四个GPU上扩展到520万个原子，其计算成本大约是其短程骨干网的两倍。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 4. Machine Learning-Assisted Discovery of Carbon-Related Defect Formation Mechanisms in Diamond

- Source: arXiv
- Date: 2026-10-19T12:51:02Z
- Venue: cond-mat.mtrl-sci
- Authors: Grace Huang, Christopher Fivecoat, Xun Xu, Mengen Wang
- Link: https://arxiv.org/abs/2610.26301v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 为了研究这种动力学驱动的过程并揭示中性电荷状态下二间隙和二空位的形成机制，我们使用密度泛函理论计算生成的小数据集微调了通用机器学习的原子间势。在通过辐照和随后的热退火产生缺陷的过程中，会产生与碳相关的缺陷，包括空位和间隙，并且可以迁移以形成新的缺陷复合体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 5. From Algebraic Completeness to Orbit Separation: Recursive Separating Invariants for Global Neural Network Potential Energy Surfaces

- Source: arXiv
- Date: 2026-10-15T11:20:02Z
- Venue: physics.chem-ph
- Authors: Yiping Hao, Jing Lou, Bina Fu, Dong H. Zhang
- Link: https://arxiv.org/abs/2610.21700v1
- Score: 9.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 这些结果确立了轨道分离作为开发全局神经网络PES的高效对称保持描述符的一个有希望的原则。
**讨论重点：** 这里，我们引入递归分离不变量（ RSI ） ，将描述符设计原理从代数完备性转变为轨道分离。基本不变量（ FI ）形成了一个代数完整的生成集，大大减少了描述符的数量，并为更大的系统启用了神经网络PES。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Instability-driven segregation of V group transition metals on HEB$_2$ grain boundaries influencing enhanced mechanical properties

- Source: arXiv
- Date: 2026-10-18T14:26:28Z
- Venue: cond-mat.mtrl-sci
- Authors: Daniil Alekseev, Viktor S. Baidyshev, Alexander G. Kvashnin
- Link: https://arxiv.org/abs/2610.25295v1
- Score: 8.0
- Match: 摘要匹配 MACE potential; 近两周发布

**中文摘要：** 五种金属在(Hf, Ta, Ti, Nb, Zr) B $_2 $ (HEB $_2 $)中共享一个共同的亚晶格。大多数高熵材料都是以烧结陶瓷的形式作为多晶材料生产的。哪些金属物种位于晶界的问题仍然未知。在这里，我们使用密度泛函理论（ DFT ）计算了五个二硼化物和HEB $_2 $中四种类型边界的晶界能$ γ_{GB} $。 我们使用COHP和HEB $_2 $六个边界的采样阳离子偏析分析了这些边界的键合，有序和一般，使用蒙特卡罗/分子动力学，具有针对该系统微调的MACE电位。根据我们的结果， $ γ_{GB} $按组分裂：组V二硼化物NbB $_2 $和TaB $_2 $在四种GB中的三种类型上形成边界，能量约为组IV的一半，范围为0.8至2.7 ，而2.5--4.8~J/m $ ^ 2 $。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS HEB $_2 $的晶界由V族金属组成，如二元化合物的边界能及其在费米能级上的键合所暗示的那样。(Hf, Ta, Ti, Nb, Zr) B $_2 $的晶界优先包括Nb和Ta。这降低了晶界能量并加强了边界。这包括下边界能量并改变NBB $_2 $和TaB $_2 $中的费米能级键。
**讨论重点：** 五种金属在(Hf, Ta, Ti, Nb, Zr) B $_2 $ (HEB $_2 $)中共享一个共同的亚晶格。大多数高熵材料都是以烧结陶瓷的形式作为多晶材料生产的。 结合关键词看，阅读时应重点关注MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Theoretical Investigation of Oxygen-Vacancy Diffusion in SrTiO$_3$ using Neural Network Potentials

- Source: arXiv
- Date: 2026-10-12T10:10:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Kazutaka Nishiguchi, Ryota Yamamoto, Seiichiro Ten-no
- Link: https://arxiv.org/abs/2610.16521v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 在这项研究中，我们使用AIMD模拟生成的参考数据集开发了原始和缺氧STO的神经网络电位（ NNP ）。训练的NNP模型准确地再现了含有氧空位的原始STO和STO的DFT参考能量、原子力和病毒。NNP还再现了总能量和氧空位形成能量的超级细胞大小依赖性，包括推断到稀释极限的形成能量。 然后使用NNP （ NNP-MD ）进行大规模和长期的MD模拟，以研究氧空位扩散。与传统的经典MD模拟相比，所得氧空位扩散系数与实验数据显示出更好的一致性。Arrhenius分析得出氧空位迁移焓为0.64 eV ，与0.67 eV的实验值非常一致。 这些结果表明，在第一原理数据上训练的NNP为研究钙钛矿氧化物中的缺陷形成和长期空位传输提供了准确且计算效率高的框架。
**讨论重点：** 在这项研究中，我们使用AIMD模拟生成的参考数据集开发了原始和缺氧STO的神经网络电位（ NNP ）。训练的NNP模型准确地再现了含有氧空位的原始STO和STO的DFT参考能量、原子力和病毒。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 8. Long-Range Machine Learning Interatomic Potentials for Defect Energetics in SrTiO$_3$

- Source: arXiv
- Date: 2026-09-30T22:33:45Z
- Venue: cond-mat.mtrl-sci
- Authors: Yee Chit Wong, Marcel F. Langer, Reinhard J. Maurer, Nicholas D. M. Hine
- Link: https://arxiv.org/abs/2610.00794v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 近年来，机器学习的原子间电位（ MLIP ）发展迅速，但大多数模型本质上仍然是半局部的，忽略了远距离静电相互作用。为了解决这一局限性，已经出现了越来越多的远程模型，但比较它们在物理现实系统上的性能的系统基准仍然很少。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 作为一个物理驱动的基准系统，我们专注于钛酸锶SrTiO $_3 $和Sr--O肖特基空位对，这是一种远程电荷相互作用发挥核心作用的材料，是研究带电极化子和其他电子和光学性质的天然垫脚石。 在此基准的基础上，我们进一步研究了在Sr-O肖特基对存在下的氧空位迁移，使用爬坡图像推动的弹性带计算和分子动力学来获得作为空位对分离函数的活化屏障，提供每个模型捕获控制缺陷输运的静电效应的能力的进一步外推测试。
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Reticulating Local Dynamics in Three-Dimensional Covalent Organic Frameworks

- Source: arXiv
- Date: 2026-10-17T03:30:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Francesco Tavani, Saber Mirzaei, M. Saeed Mirzaei, Jian Yin, Yen-hsu Lin, Caden Myers
- Link: https://arxiv.org/abs/2610.24418v1
- Score: 7.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：In covalent organic frameworks (COFs), the geometry of the building units predetermines the structure of the framework, yet comparable design principles relating the COF linkers to the local motions that govern guest adsorption and diffusion as well as mechanical response have remained beyond reach. Here, we combine synchrotron X-ray pair distribution function (PDF) analysis with molecular dynamics (MD) simulations accelerated by machine learning interatomic potentials to resolve and compare the local dynamics of two three-dimensional imine-linked COFs, chosen to differ in the geometry and rigidity of one of their two building units. Both are constructed from the same 4-connected square planar linker, $4,4',4'',4'''$-(pyrene-1,3,6,8-tetrayl)tetraaniline (PyTTA), reticulated with the 12-connected nanographene hexakis{[3,5-bis($p$-formylphenyl)-4,6-dimethoxyphenyl]}hexabenzocoronene to give COF-412, {[(HBC-LA$_{12}$)(PyTTA)$_3$]}$_{\mathit{imine}}$, and with the 6-connected triptycene 2,3,6,7,14,15-hexakis(4-formylphenyl)triptycene to give COF-564, {[(Trip-CHO)$_2$(PyTTA)$_3$]}$_{\mathit{imine}}$. The PDF-MD approach resolves the amplitude, the time scale, and the spatial extent of the motion of all COF linkers, separating the limited libration of the fused aromatic cores from the larger reorientational tilts of the pendant aryl rings they carry and from the translation of whole linkers within the net. The simulations further reveal that exchanging the nanographene- for the triptycene-based linker tunes the equilibrium tilt and the positional probability density of PyTTA, raising the tilt amplitude of its linker partner, and, notably, strengthens the coupling between the translations of neighbouring linkers. This approach provides a blueprint for underst...
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Benchmarking machine-learning interatomic potentials using classical force fields

- Source: arXiv
- Date: 2026-10-09T18:56:31Z
- Venue: cond-mat.mtrl-sci
- Authors: Johannes Sandberg, Geneviève Dusson, Julien Lam
- Link: https://arxiv.org/abs/2610.14239v1
- Score: 7.0
- Match: 摘要匹配 neural network potential; 摘要匹配 MACE potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We propose a rational comparison between several well-known machine-learning interatomic potentials (linear atomic cluster expansion, the Behler-Parrinello high-dimensional neural network potential, and the graph neural network-based MACE potential) by testing their performance for fitting classical potentials such as the Lennard-Jones and Stillinger-Weber potential. With this we assess their advantages and limitations regarding several aspects: varying training dataset size, robustness to noise, carbon footprint, as well as the ability to reproduce the radial distribution function as an example observable. Overall the MACE models are shown to most accurately reproduce the potential energy surface, with little sign of overfitting, but at a significant computational cost, highlighting important questions regarding the choice of models in computational materials science.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注神经网络势、MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Two-Dimensional Magnetic Materials from Ferromagnetism to Altermagnetism: Fabrication, Symmetry, Evidence, and Device Readiness

- Source: arXiv
- Date: 2026-10-28T09:04:30Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.app-ph
- Authors: Guojian Zhao, Ziang Meng, Li Liu, Zhiyuan Duan, Jingyu Li, Sixu Jiang
- Link: https://arxiv.org/abs/2610.38491v1
- Score: 32.0
- Match: 标题匹配 ferromagnetism; 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Atomically thin magnets are governed by composition, thickness, stacking, strain, defects, substrates, ferroic order, and interfaces. This Review organizes two-dimensional (2D) magnetism using net magnetization and momentum-space spin splitting or spin-polarization patterns as primary coordinates, supplemented by sublattice structure and the symmetry relations between opposite-spin sublattices. Ferromagnets generally carry a net moment; ferrimagnets can be fully compensated. Conventional antiferromagnets may retain spin-degenerate bands, while altermagnets permit nonrelativistic alternating spin splitting under dimension-specific symmetry constraints. M1-M4 reporting classes introduced here distinguish layer-resolved atomically thin forms, non-layer-resolved thin flakes or films, bulk benchmarks, and theoretical candidates or design routes; the evidence category and ordering-temperature provenance are reported independently. Current experimental support for altermagnetism comes mainly from M2 thin-film and M3 bulk benchmarks, leaving a fully verified atomically thin M1 altermagnetic phase as an open experimental goal. Most proposed monolayer and few-layer systems therefore fall within M4, and contested cases clarify the measurements needed for phase assignment. Device readiness is compared qualitatively using operating temperature, readout, switching, domain control, stability, scalability, interface sensitivity, and integration difficulty. Reliable phase assignment and device assessment require complementary measurements from the same material form under matched conditions, ideally on the same specimen or in situ.
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Light-induced chiral altermagnets from conventional antiferromagnets

- Source: arXiv
- Date: 2026-10-29T16:40:19Z
- Venue: cond-mat.mtrl-sci
- Authors: Jorge Cardenas-Gamboa, Devika Jayadeep, Aritz Leonardo, Gregory A. Fiete, Jeroen van den Brink, Maia G. Vergniory
- Link: https://arxiv.org/abs/2610.40410v1
- Score: 22.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Altermagnets combine compensated collinear magnetic order with momentum-dependent nonrelativistic spin splitting, offering new opportunities for spintronic applications. Here, we propose a route to optically induce altermagnetism through coherent lattice control. Using symmetry analysis, we identify phonon distortions that lift the spin degeneracy of conventional antiferromagnets while preserving the rotational symmetries connecting opposite-spin sublattices. Among these, geometric chiral phonons provide a particularly appealing pathway, linking the emergence of altermagnetism to structural chirality. Taking Fe$_2$TeO$_6$ as a prototype, we demonstrate that a linearly polarized mid-infrared pulse can drive a structural instability through negative biquadratic coupling between an infrared-active phonon and an optically silent, symmetry-breaking mode. First-principles-based lattice dynamics reveal the emergence of a transient chiral distortion, while electronic-structure calculations establish that the light-induced structure exhibits nonrelativistic spin splitting characteristic of altermagnetism. Our results establish a symmetry-guided pathway toward the ultrafast optical control of altermagnetic states through nonlinear phononics.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Topological Quantum Spin Liquids in a Ladder with Majorana fermions and p-wave Superconductivity

- Source: arXiv
- Date: 2026-10-29T15:43:52Z
- Venue: cond-mat.str-el, cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Magali Korolev, Fan Yang, Erik S. Sørensen, Karyn Le Hur
- Link: https://arxiv.org/abs/2610.40297v1
- Score: 19.0
- Match: 标题匹配 quantum spin liquid; 摘要匹配 density matrix renormalization group; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：In this article, we address the possibility of topological quantum spin liquids with only short-range (spin) correlations in the whole phase diagram in a ladder system, through an exactly solvable model which represents a generalization of the two-dimensional Kitaev honeycomb spin model to a ribbon geometry. This system gives rise to $\mathbb{Z}_2$ gauge fields emerging in a static way in the ground state through Majorana fermions which then produce either $0$ or $π$ flux. Through a quantum field theory perspective, mathematical and Density Matrix Renormalization Group results, we present our progress on the geometrical, topological and physical classification of this model through observables navigating on the whole phase diagram presenting three spin-liquid phases with a spin gap and a metallic phase in the sense of Majorana fermions. We propose a bulk-edge correspondence revealing the presence of protected zero-energy Majorana fermions at the edge in the phases with a gap and revealing also the presence of itinerant Majorana fermions in the bulk in the topological liquid phase. The proposed approach allows us to distinguish between properties of the brickwall ladder giving rise to a special line and those of the square ladder allowing for the gapless Majorana liquid phase. This model gives some hope on finding solutions for topological quantum spin models, e.g. with $π$ flux, on a square lattice geometry. This approach also allows for a correspondence onto models of topological superconductivity.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注量子自旋液体、密度矩阵重整化群相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 4. Pulse Laser Deposited GaFeO3 Thin Film Grown on FTO: Correlated Ferroic Orders and Strong Magnetodielectric Coupling at Room Temperature

- Source: arXiv
- Date: 2026-10-29T09:33:58Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Ishita Jana, Sourav Sarkar, Soham Saha, Kalyan Mandal
- Link: https://arxiv.org/abs/2610.39696v1
- Score: 18.0
- Match: 摘要匹配 multiferroic; 摘要匹配 magnetoelectric coupling; 摘要匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注多铁性、磁电耦合、铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 5. Nodal magnon spin current at an antiferromagnet/altermagnet junction

- Source: arXiv
- Date: 2026-10-29T02:29:57Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Koki Mizuno
- Link: https://arxiv.org/abs/2610.39206v1
- Score: 18.0
- Match: 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We investigate the thermally driven magnon spin current across a junction between a $d$-wave altermagnet (AM) and a ferromagnet (FM) or an antiferromagnet (AFM). The current consists of a component independent of the interface angle and an angularly dependent component with the $d$-wave form. For a sublattice-symmetric interface, the two junctions behave oppositely under reversal of the altermagnetic domain: in the FM/AM junction the angularly dependent component is odd and cancels on averaging over the domains, whereas in the AFM/AM junction the angularly independent component vanishes by symmetry and the angularly dependent component survives the domain average at a fixed Néel vector of the AFM. Both follow from a selective tunneling: a pair of spins bonded across the interface transmits magnons when the spins are parallel and not when antiparallel, which makes the AFM/AM junction a magnon valve: the configuration in which the bonded spins are antiparallel blocks the current up to the sublattice admixture of the magnons. The anisotropic tunneling is detectable as the sign reversal of the current between the interfaces normal to $[310]$ and $[130]$, and the valve reads the Néel vector of the altermagnet relative to that of the antiferromagnet through the magnitude of the current at a fixed interface.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Electronic liquid crystals and superconductivity from doping a moiré Mott insulator

- Source: arXiv
- Date: 2026-10-29T13:07:04Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Yichi Zhang, Yiyu Xia, Zhongdong Han, Jekwan Lee, Brandon Bauer, Kenji Watanabe
- Link: https://arxiv.org/abs/2610.39978v1
- Score: 16.0
- Match: 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Spin-Orbit Coupling Response Theory within the Oriented Spin Space Group Framework

- Source: arXiv
- Date: 2026-10-29T14:34:20Z
- Venue: cond-mat.mtrl-sci
- Authors: Yuntian Liu, Xiaobing Chen, Yutong Yu, Jesús Etxebarria, J. Manuel Perez-Mato, Qihang Liu
- Link: https://arxiv.org/abs/2610.40149v1
- Score: 15.0
- Match: 摘要匹配 multiferroic; 摘要匹配 magnetoelectric coupling; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Spin-orbit coupling (SOC) plays a pivotal role in a broad range of phenomena in condensed matter physics. The recently developed spin space group theory offers a new perspective for characterizing the fundamental symmetry-breaking features of SOC-related phenomena, yet its full potential remains to be explored. Here, we provide a general framework that relates the SOC-induced symmetry breaking to modifications of physical properties and emergence of new physical effects. This approach incorporates the recently developed oriented spin space group (OSSG) formalism, which can explicitly describe the symmetry reduction induced by SOC. By parameterizing the SOC Hamiltonian using a SOC tensor that connects real and spin spaces, an expansion in terms of the SOC components can be constructed for the response tensor describing any physical quantity. This framework determines not only whether a SOC-induced response is symmetry allowed, but also the lowest order in SOC at which it emerges and its dependence on magnetic anisotropy. As representative applications, we analyze the magnetoelectric coupling in Type-II multiferroics and show that magnetically induced electric polarization in different systems can be the result of SOC effects of different orders, and can exhibit varying characteristics of magnetic anisotropy. We further apply this theory to the anomalous Hall effect and spin magnetization in antiferromagnets, demonstrating that their distinct transformation properties under the OSSG allow a large anomalous Hall response to coexist with weak spin magnetization. A high-throughput analysis of materials in the MAGNDATA database identifies several symmetry-based material classes favorable for this coexistence. Overall, the proposed framework provides a unifie...
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注多铁性、磁电耦合相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. Collective sliding relaxor ferroelectricity across thousand-layer van der Waals superstructures

- Source: arXiv
- Date: 2026-10-28T21:17:54Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.app-ph
- Authors: Nianze Shang, Cuiju Yu, Yucai Lin, Juan C. Arias-Muñoz, Jiajie Qi, Quanlin Guo
- Link: https://arxiv.org/abs/2610.38928v1
- Score: 15.0
- Match: 标题匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Relaxor ferroelectrics are among the most important electromechanical materials owing to their exceptionally large electrostrictive responses. However, conventional relaxor behavior is generally associated with chemical complexity and structural disorder, where local compositional fluctuations generate polar nanoregions, making the microscopic origin of this behavior difficult to control and engineer. Here we report sliding relaxor ferroelectricity (S-RFE), a previously unknown relaxor state in which engineered stacking-phase heterogeneity enables cooperative interlayer sliding to generate collective relaxor behavior. Through stacking-phase engineering in rhombohedral boron nitride, we create sliding domains that act as structural analogues of polar nanoregions and cooperatively align under an electric field through interlayer sliding. This collective state produces reversible electromechanical deformation of up to approximately $-1.6\%$ with negligible hysteresis in approximately 300-nm-thick crystals, corresponding to approximately 1000 atomic layers. The resulting electrostriction coefficient ($Q_{33}$ of approximately $1200\,\mathrm{m}^{4}\mathrm{C}^{-2}$) exceeds those of most crystalline electrostrictors by orders of magnitude. Unlike conventional relaxors, whose electromechanical response is often suppressed by dipolar freezing at low temperatures, S-RFE remains active down to 1.6 K and maintains giant electromechanical functionality. Our results establish sliding relaxor ferroelectricity as a new route to relaxor behavior and reveal how atomic-scale interlayer motion can be amplified into collective mesoscale functionality across approximately one thousand layers, providing a materials-by-design platform for electromechanical, photonic, and qua...
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 9. The Flexoelectric Twist: Persistence of Heavy Fermion Picture in Small-Angle Twisted Bilayer Graphene

- Source: arXiv
- Date: 2026-10-28T05:44:01Z
- Venue: cond-mat.mes-hall
- Authors: Qirong Yao, Ka Cheuk Fan, Tianyu Qiao, Hao Shi, Xi Dai, Berthold Jäck
- Link: https://arxiv.org/abs/2610.38305v1
- Score: 15.0
- Match: 标题匹配 heavy fermion; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Twisted bilayer graphene (TBG) near the first magic angle ($θ\approx1.05^{\circ}$) hosts flat bands that provide a fertile ground for exploring strongly correlated and topological phases. At smaller twist angles ($θ<1^{\circ}$), attice relaxation profoundly alters the moiré landscape. The extent to which moiré lattice reconstruction at different length scales affects the electronic structure through electro-mechanical coupling remains unresolved. Here, using scanning tunneling microscopy on small-angle TBG devices ($θ\approx0.3-0.7^{\circ}$), we observe a pronounced $dI/dV$ peak at the AA site of the moiré lattice on top of a spectrum that is asymmetric about the charge neutrality point, lattice reconstruction over moiré lattice length scales, as well as a dilation of the atomic lattice at the AA sites. We demonstrate at a phenomenological level that the inclusion of moiré lattice reconstruction supports compact localized heavy fermion $f-$ states localized at AA sites. The additional inclusion of atomic lattice dilation enerates a strong flexo-electric response that explicitly breaks particle-hole symmetry, pushing compact, localized $f$-states at the AA sites down in energy. Consequently, these heavy fermion states energetically coexist with itinerant $c$-electrons at the AB/BA sites. Our spatially resolved spectroscopic measurements quantitatively visualize this coexistence, confirming the persistence of the heavy fermion model in the small-angle regime $θ<1^{\circ}$. Our findings provide microscopic insights into how flexo-electricity affects the low-energy electronic structure of small-angle TBG. More broadly, our study establishes small-angle TBG as a new class of moiré materials to explore the interacting Kondo lattice problem with high tunabili...
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注重费米子相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Quasi-Phases of Quantum Matter

- Source: arXiv
- Date: 2026-10-29T17:32:53Z
- Venue: cond-mat.str-el, cond-mat.stat-mech, quant-ph
- Authors: Nick G. Jones, Paul Fendley, Nathanan Tantivasadakarn, Ruben Verresen
- Link: https://arxiv.org/abs/2610.40526v1
- Score: 12.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注量子多体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。
